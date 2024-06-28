import { createStore } from 'vuex';
import api from '@/api';  
import axios from 'axios'
export default createStore({
  state: {
    isAuthenticated: false,
    accessToken: localStorage.getItem('accessToken') || null,
    refreshToken: localStorage.getItem('refreshToken') || null,
    errors: []
  },
  mutations: {
    setAuthentication(state, { isAuthenticated, accessToken, refreshToken }) {
      state.isAuthenticated = isAuthenticated;
      state.accessToken = accessToken;
      state.refreshToken = refreshToken;
    },
    clearAuthentication(state) {
      state.isAuthenticated = false;
      state.accessToken = null;
      state.refreshToken = null;
    },
    setErrors(state, errors) {
      state.errors = errors;
    }
  },
  actions: {
    async login({ commit }, { username, password }) {
      try {
        const formData = { username, password };
        const response = await api.post('/auth/jwt/create/', formData); 

        if (response.status === 200) {
          const { access, refresh } = response.data;
          commit('setAuthentication', { isAuthenticated: true, accessToken: access, refreshToken: refresh });
          localStorage.setItem('accessToken', access);
          localStorage.setItem('refreshToken', refresh);
          api.defaults.headers.common['Authorization'] = `Bearer ${access}`;
          return { success: true };
        } else {
          commit('setErrors', [response.data.detail || 'Login failed. Please check your credentials.']);
          return { success: false };
        }
      } catch (error) {
        console.error('Error during login:', error);
        commit('setErrors', ['Something went wrong. Please try again.']);
        return { success: false };
      }
    },
    async loginWithGoogle({ commit }, token_id) {
      try {
        const response = await api.post('/auth/google/', { token_id });  

        if (response.ok) {
          const data = await response.json();
          const { access, refresh } = data;
          commit('setAuthentication', { isAuthenticated: true, accessToken: access, refreshToken: refresh });
          localStorage.setItem('accessToken', access);
          localStorage.setItem('refreshToken', refresh);
          api.defaults.headers.common['Authorization'] = `Bearer ${access}`;
          return { success: true };
        } else {
          console.error('Failed to register with backend:', response.statusText);
          return { success: false };
        }
      } catch (error) {
        console.error('Error sending token to backend:', error);
        return { success: false };
      }
    },
    logout({ commit }) {
      commit('clearAuthentication');
      localStorage.removeItem('accessToken');
      localStorage.removeItem('refreshToken');
      delete axios.defaults.headers.common['Authorization'];
    }
  },
  getters: {
    isAuthenticated: state => state.isAuthenticated,
    accessToken: state => state.accessToken,
    refreshToken: state => state.refreshToken,
    errors: state => state.errors
  }
});
