import Vue from 'vue'
import Router from 'vue-router'
import Login from './components/user/login.vue'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/login', component: Login
    }
  ]

})
