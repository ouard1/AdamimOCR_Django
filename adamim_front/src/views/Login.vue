<template>
    <div class="page-login">
    <div class="columns">
      <div class="column is-4 is-offset-4">
        <h1 class="title" style="color: aliceblue;">Log in</h1>
  
      
      <form @submit.prevent="submitForm">
        <div class="field">
          <label for="username" class="label">Username</label>
          <div class="control">
            <input id="username" type="text" class="input" v-model="username" placeholder="Enter your username">
          </div>
        </div>
  
  
        <div class="field">
          <label for="password" class="label">Password</label>
          <div class="control">
            <input id="password" type="password" class="input" v-model="password" placeholder="Enter your password">
          </div>
        </div>
  
        <div v-if="errors.length" class="notification is-danger">
          <p v-for="error in errors" :key="error">{{ error }}</p>
        </div>
  
        <div class="field">
          <div class="control">
            <button type="submit" class="button is-link">Login</button>
          </div>
        </div>
      </form>
  
     
      
      <p style="color: white; text-align: center; margin-top: 10px;">Or continue with google </p>
      <div id="g_id_onload"
           data-client_id="146908205548-qsu2ppsmnju9cjsk1qgrngm3n09bhrd2.apps.googleusercontent.com"
           data-login_uri="https://adamim-ocr.vercel.app"
           data-callback="handleCredentialResponse"
           data-cancel_on_tap_outside="false">
      </div>
      <p style="color: white; text-align: center; margin-top: 10px;">Don't have an account? <router-link to="/sign-up">Click here to sign up</router-link></p>
      </div>
    </div>
  </div>
  
   
  </template>
  
  <script>
import axios from 'axios';
import { useStore } from 'vuex';

export default {
  data() {
    return {
      username: '',
      password: '',
      errors: []
    };
  },
  mounted() {
    
    this.loadGoogleOneTapClient();
  },
  methods: {
    loadGoogleOneTapClient() {
      const script = document.createElement('script');
      script.src = 'https://accounts.google.com/gsi/client';
      script.onload = () => {
        window.google.accounts.id.initialize({
          client_id: process.env.VUE_APP_GOOGLE_CLIENT_ID, 
          callback: this.handleCredentialResponse,
          login_uri: 'https://adamim-ocr.vercel.app', 
          cancel_on_tap_outside: false
        });
        this.renderGoogleOneTapButton();
      };
      document.head.appendChild(script);
    },
    renderGoogleOneTapButton() {
      window.google.accounts.id.renderButton(
        document.getElementById('g_id_onload'),
        { theme: 'filled_blue', size: 'large', text: 'continue_with' }
      );
    },
    async handleCredentialResponse(response) {
      if (response.clientId && response.credential && response.select_by) {
        const token_id = response.credential;
        this.sendTokenToBackend(token_id);
        
      } else {
        console.error('Invalid response from Google authentication');
      }
    },
    async sendTokenToBackend(token_id) {
      try {
        const response = await fetch('https://adamimocr.onrender.com/api/auth/google/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            token_id: token_id
          })
        });

        if (response.ok) {
          const data = await response.json();
          const { access, refresh } = data;
          this.setAuthTokens(access, refresh);
        } else {
          console.error('Failed to register with backend:', response.statusText);
          
        }
      } catch (error) {
        console.error('Error sending token to backend:', error);
      
      }
    },
    async submitForm() {
      this.errors = [];

      if (!this.username.trim()) {
        this.errors.push('Username is required.');
      }

      if (!this.password.trim()) {
        this.errors.push('Password is required.');
      }

      if (this.errors.length === 0) {
        try {
          const formData = {
            username: this.username,
            password: this.password
          };

          const response = await axios.post('https://adamimocr.onrender.com/api/auth/jwt/create/', formData);
          
          if (response.status === 200) {
            const { access, refresh } = response.data;
            this.setAuthTokens(access, refresh);
          } else {
            this.errors.push(response.data.detail || 'Login failed. Please check your credentials.');
          }
        } catch (error) {
          console.error('Error during login:', error);
          this.errors.push('Something went wrong. Please try again.');
        }
      }
    },
    setAuthTokens(access, refresh) {
      
      this.$store.commit('setAuthentication', { isAuthenticated: true, accessToken: access, refreshToken: refresh });
      
      localStorage.setItem('accessToken', access);
      localStorage.setItem('refreshToken', refresh);
      
      this.$router.push('/Api');
    }
  }
};
</script>

<style>

.login-container {
  max-width: 400px;
  margin: 0 auto;
  padding: 20px;
}
</style>
