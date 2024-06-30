<template>
    <div class="page-sign-up">
      <div class="columns">
        <div class="column is-4 is-offset-4">
          <h1 class="title" style="color: aliceblue;">Sign up</h1>
  
          <form @submit.prevent="submitForm">
            <div class="field">
              <label class="label">Username</label>
              <div class="control">
                <input type="text" class="input" v-model="username">
              </div>
            </div>
  

            <div class="field">
              <label class="label">Password</label>
              <div class="control">
                <input type="password" class="input" v-model="password">
              </div>
            </div>
  
            <div class="field">
              <label class="label">Repeat Password</label>
              <div class="control">
                <input type="password" class="input" v-model="password2">
              </div>
            </div>
  
            <div class="notification is-danger" v-if="errors.length">
              <p v-for="error in errors" :key="error">{{ error }}</p>
            </div>
  
            <div class="field">
              <div class="control">
                <button class="button is-link">Sign up</button>
              </div>
            </div>
  
            <hr>
            
              <p style="font-family: 'poppins', sans-serif; color: white; text-align: center;">Or continue with google </p>
              
      <div style="display: flex; justify-content: center;" id="g_id_onload"
           data-client_id="146908205548-qsu2ppsmnju9cjsk1qgrngm3n09bhrd2.apps.googleusercontent.com"
           data-login_uri="https://adamim-ocr.vercel.app"
           data-callback="handleCredentialResponse"
           data-cancel_on_tap_outside="false">
      </div>
          </form>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  import { toast } from 'bulma-toast';
  
  export default {
    name: 'SignUp',
    data() {
      return {
        username: '',
        password: '',
        password2: '',
        errors: [],
        accessToken: null,
        refreshToken: null
      };
    },
    mounted() {
      document.title = 'Sign Up | Kalima';
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
        { theme: 'filled_white', size: 'large', text: 'continue_with' }
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
  
        if (this.password !== this.password2) {
          this.errors.push('Passwords do not match.');
        }
  
        if (this.errors.length === 0) {
          try {
            const formData = {
              username: this.username,
              password: this.password,
              password2: this.password2
            };
  
            const response = await axios.post('https://adamimocr.onrender.com/api/auth/register/', formData);
  
            if (response.status === 201) {
              toast({
                message: 'Account created, please log in',
                type: 'is-success',
                dismissible: true,
                pauseOnHover: true,
                duration: 2000,
                position: 'bottom-right',
              });
  
              this.$router.push('/log-in');
            } else {
              this.errors.push(response.data.detail || 'Sign up failed. Please check your inputs.');
            }
          } catch (error) {
            console.error('Error during sign up:', error);
            this.errors.push('Something went wrong. Please try again.');
          }
        }
      },
      handleGoogleLoginSuccess() {
        this.$router.push('/api');
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
  .label {
    color: white;
  }
  
  img {
    background: transparent;
  }
  </style>
  
