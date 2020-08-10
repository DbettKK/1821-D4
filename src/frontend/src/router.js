import Vue from 'vue'
import Router from 'vue-router'
import Login from './components/user/login.vue'
import User from './components/user/UserInfo.vue'
import Home from './components/user/home.vue'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/Info', component: User
    },
    {
      path: '/Login', component: Login
    },
    {
      path: '/', component: Home
    }
  ]

})
