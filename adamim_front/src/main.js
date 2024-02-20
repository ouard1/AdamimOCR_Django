import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios'
import vue3GoogleLogin from 'vue3-google-login'


axios.defaults.baseURL = 'http://127.0.0.1:8000'

createApp(App).use(store).use(router).use(vue3GoogleLogin, {
  clientId: '971420903342-6mmaj85rb26ufe782p0aiskqo3b8pc8d.apps.googleusercontent.com'
}).mount('#app')
