<template>
  <div id="wrapper">
    <nav class="navbar" style="background-color: rgba(255,255,255,0.8);">
      <div class="navbar-brand">
        <router-link to="/" class="navbar-item">
          <a class="navbar-item">
            <img src="@/assets/logo.png" alt="Logo Kalima">
          </a>
          <strong>Kalima</strong></router-link>
        <a class="navbar-burger" aria-label="menu" aria-expanded="false" data-target="navbar-menu" @click="showMobileMenu = !showMobileMenu">
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
        </a>
      </div>
      
      <div class="navbar-menu" id="navbar-menu" v-bind:class="{'is-active': showMobileMenu }">
        
        <div class="navbar-end">

          
          <div class="navbar-item">
            <div class="buttons">
              <template v-if="$store.state.isAuthenticated">
                <router-link to="/Api" class="button is-success">Access Kalima</router-link>
                <button @click="logout()" class="button is-danger">Log out</button>
              </template>

              <template v-else>
                <button class="button" @click="openModal">Log in <i class="fa-solid fa-right-to-bracket ml-2" style="color: #FFD43B;"></i></button>
                
              </template>
            </div>
          </div>
        </div>
      
      </div>

    </nav>

  <section class="section mt-6">
    <router-view/>

      <!-- The Modal Is Here -->
      <div>
        <div class="modal" :class="{'is-active': modalOpen}">
          <div class="modal-background" @click="closeModal"></div>
          <div class="modal-content">
            <!-- Pass the closeModal method as a prop to the Login component -->
            <Login @loginSuccess="handleLoginSuccess" />
          </div>
          <button class="modal-close is-large" @click="closeModal"></button>
        </div>
      </div>
    </section>
  
  <footer class="footer has-background-link">
    <p class="has-text-centered" style="color: white; font-size: 1.2em;" > <a href="https://nara.dsru.cerist.dz/" style="color: white;">Copyright Data Science & Applications Unit (CERIST)</a></p>
  </footer>
  </div>
</template>

<style lang="scss">
@import '../node_modules/bulma';
</style>

<script>
import Login from '@/components/Login'
import axios from 'axios'

export default {
  data() {
    return {
      showMobileMenu: false,
      modalOpen: false
    }
  },
  components: {
    Login
  },
  methods: {
    openModal() {
      this.modalOpen = true;
    },
    closeModal() {
      this.modalOpen = false;
    },
    logout() {
      this.$store.dispatch('logout');
      this.$router.push('/');
    },
    handleLoginSuccess() {
      this.closeModal();
    }
  }
}
</script>



<style lang="scss">

/* Add this to your existing style block */
#app {
  display: flex;
  flex-direction: column;
  height: 100vh;
  background-image: url('@/assets/bg.jpg');
  background-repeat: no-repeat;
  background-size: cover;
}

section, footer {
  flex: 1;
  overflow-y: auto;
}

.modal {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  display: none;
  align-items: center;
  justify-content: center;
  z-index: 999; /* Ensure the modal is on top of other elements */
}

.modal-background {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5); /* Add a semi-transparent background to create the overlay effect */
}

.modal-content {
  font-family: 'inter',sans-serif;
  background-color: white;
  padding: 20px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  z-index: 1000; /* Ensure the modal content is on top of the background */
  border-radius: 10px;
}

.modal-close {
  position: absolute;
  top: 10px;
  right: 10px;
  font-size: 24px;
  cursor: pointer;
  z-index: 1001; /* Ensure the close button is on top of the modal content */
}

.navbar {
  position: fixed;
  width: 100%;
  top: 0;
  z-index: 1000;
}

</style>