import Vue from 'vue'
import Router from 'vue-router'
import Login from './components/user/login.vue'
import User from './components/user/UserInfo.vue'
import Home from './components/user/home.vue'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/Info', 
      component: User, 
      name:'Info',
      meta:{title:'个人空间'}
    },
    {
      path: '/Login', 
      component: Login,
      name: 'Login',
      meta:{title:'用户登录'}
    },
    {
      path: '/', 
      component: Home,
      name: 'Home',
      meta:{title:'金刚石文档编辑器'}
    }
  ]

})
