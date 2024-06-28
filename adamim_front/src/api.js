import axios from 'axios';

// Configuration de l'instance Axios
const api = axios.create({
  baseURL: 'http://127.0.0.1:8000/api',
});

// Ajouter un intercepteur pour rafraîchir le token avant l'expiration
api.interceptors.response.use(
  response => response,
  async error => {
    const originalRequest = error.config;

    if (error.response.status === 401 && !originalRequest._retry) {
      originalRequest._retry = true;
      try {
        const refreshToken = localStorage.getItem('refreshToken');
        const response = await axios.post('/auth/jwt/refresh/', { refresh: refreshToken });
        const { access } = response.data;

        // Stocker le nouveau access token et mettre à jour les en-têtes de la requête
        localStorage.setItem('accessToken', access);
        api.defaults.headers.common['Authorization'] = `Bearer ${access}`;
        originalRequest.headers['Authorization'] = `Bearer ${access}`;

        // Refaire la requête originale avec le nouveau token
        return api(originalRequest);
      } catch (error) {
        console.error('Le token de rafraîchissement a échoué:', error);
        // Gérer l'échec du rafraîchissement (par exemple, rediriger vers la page de connexion)
        return Promise.reject(error);
      }
    }
    return Promise.reject(error);
  }
);

export default api;


