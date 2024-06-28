import axios from 'axios';

const api = axios.create({
  baseURL: 'https://adamimocr.onrender.com/api',
});


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

        
        localStorage.setItem('accessToken', access);
        api.defaults.headers.common['Authorization'] = `Bearer ${access}`;
        originalRequest.headers['Authorization'] = `Bearer ${access}`;

        
        return api(originalRequest);
      } catch (error) {
        console.error('Le token de rafraîchissement a échoué:', error);
        
        return Promise.reject(error);
      }
    }
    return Promise.reject(error);
  }
);

export default api;


