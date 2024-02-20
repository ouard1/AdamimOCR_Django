import { createRouter, createWebHistory } from 'vue-router';
import HomeView from '../views/HomeView.vue';
import SignUp from '../views/SignUp.vue';
import Login from '../views/Login.vue';
import Api from '../views/Api.vue';
import store from '../store';

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/sign-up',
    name: 'signup',
    component: SignUp
  },
  {
    path: '/log-in',
    name: 'Login',
    component: Login
  },
  {
    path: '/Api',
    name: 'Api',
    component: Api,
    meta: {
      requireLogin: true
    }
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
});

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requireLogin) && !store.state.isAuthenticated) {
    next({ name: 'Login', query: { to: to.path } });
  } else {
    next();
  }
});

export default router;
