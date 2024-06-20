<template>
  <div>
    <h1>Google One Tap Example</h1>
    <div id="g_id_onload"
         data-client_id="146908205548-qsu2ppsmnju9cjsk1qgrngm3n09bhrd2.apps.googleusercontent.com"
         data-login_uri="http://localhost:8080"
         data-callback="handleCredentialResponse"
         data-cancel_on_tap_outside="false">
    </div>
    <div v-if="token">
      <p>Signed in with token: {{ token }}</p>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      token: null
    };
  },
  mounted() {
    // Load Google One Tap client
    this.loadGoogleOneTapClient();
  },
  methods: {
    loadGoogleOneTapClient() {
      const script = document.createElement('script');
      script.src = 'https://accounts.google.com/gsi/client';
      script.onload = () => {
        window.google.accounts.id.initialize({
          client_id: '146908205548-qsu2ppsmnju9cjsk1qgrngm3n09bhrd2.apps.googleusercontent.com', // Replace with your actual client ID
          callback: this.handleCredentialResponse,
          login_uri: 'http://localhost:8080', // Replace with your app's URI
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
    handleCredentialResponse(response) {
      if (response.clientId && response.credential && response.select_by) {
        const access_token = response.credential;
        this.sendTokenToBackend(access_token);
        this.token = access_token; // Optionally store or display the token
      } else {
        console.error('Invalid response from Google authentication');
      }
    },
    async sendTokenToBackend(access_token) {
      try {
        const response = await fetch('http://127.0.0.1:8000/api/register-by-access-token/social/google-oauth2/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            access_token: access_token
          })
        });

        if (response.ok) {
          const data = await response.json();
          console.log('Response from backend:', data);
          // Handle success response from backend
        } else {
          console.error('Failed to register with backend:', response.statusText);
          // Handle backend failure
        }
      } catch (error) {
        console.error('Error sending token to backend:', error);
        // Handle fetch error
      }
    }
  }
};
</script>

<style>
/* Add styling for your button or use default styling from Google */
</style>
