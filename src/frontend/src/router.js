import Vue from 'vue'
import Router from 'vue-router'
import Login from './components/user/login.vue'
import User from './components/user/UserInfo.vue'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/Info', component: User
    },
    {
      path: '/Login', component: Login
    }
  ]

})
