import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios'
import vue3GoogleLogin from 'vue3-google-login'

axios.defaults.baseURL = 'http://127.0.0.1:8080'

createApp(App)
  .use(store)
  .use(router)
  .use(vue3GoogleLogin, {
    clientId:  '146908205548-qsu2ppsmnju9cjsk1qgrngm3n09bhrd2.apps.googleusercontent.com'
  })
  .mount('#app')