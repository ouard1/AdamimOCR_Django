<template>
  <div id="wrapper">
    <nav class="navbar is-dark">
      <div class="navbar-brand">
        <router-link to="/" class="navbar-item"><strong>Adamim OCR</strong></router-link>
        <a class="navbar-burger" aria-label="menu" aria-expanded="false" data-target="navbar-menu" @click="showMobileMenu = !showMobileMenu">
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
        </a>
      </div>
      
      <div class="navbar-menu" id="navbar-menu" v-bind:class="{'is-active': showMobileMenu }">
        <div class="navbar-end">
          <router-link to="/about" class="navbar-item">Features</router-link>
          <router-link to="/about" class="navbar-item">About</router-link>
          
          <div class="navbar-item">
            <div class="buttons">
              <template v-if="$store.state.isAuthenticated">
                <router-link to="/my-account" class="button is-light">My Account</router-link>
              </template>

              <template v-else>
                <router-link to="/log-in" class="button is-light">Log in</router-link>
              </template>
            </div>
          </div>
        </div>
      </div>

    </nav>

  <section class="section">
    <router-view/>
  </section>
  
  <footer class="footer">
    <p class="has-text-centered"> Copyright Data Science & Applications Unit (CERIST) 2024</p>
  </footer>
  </div>
</template>

<style lang="scss">
@import '../node_modules/bulma';
</style>

<script>
import axios from 'axios'
export default {
  data() {
    return{
      showMobileMenu: false,
    }
  },
beforeCreate() {
  this.$store.commit('initializeStore')
  const token = this.$store.state.token

  if (token) {
    axios.defaults.headers.common['Authorization'] = "Token " + token
  } else {
    axios.defaults.headers.common['Authorization'] = ""
  }
},
}
</script>