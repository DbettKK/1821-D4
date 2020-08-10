import Vue from 'vue'
import Router from 'vue-router'
import Login from './components/user/login.vue'
import User from './components/user/UserInfo.vue'
import Home from './components/user/home.vue'
import Welcome from './components/user/welcome.vue'

Vue.use(Router)

const router = new Router({
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
      meta:{title:'金刚石文档编辑器'},
      redirect: '/welcome',
      children: [{path: '/welcome', component: Welcome}]
    }
  ]

})

//路由导航守卫
router.beforeEach((to, from, next) => {
  if (to.path === '/login') return next();
  //获取token
  const tokenStr = window.sessionStorage.getItem('token')
  if (!tokenStr) return next('/login')
  next()
})

export default router
