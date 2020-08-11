import Vue from 'vue'
import Router from 'vue-router'
import Login from './components/user/login.vue'
import Register from './components/user/register.vue'
import User from './components/user/UserInfo.vue'
import Home from './components/user/home.vue'
import Welcome from './components/user/welcome.vue'
import Ue from './components/edit/ue.vue'

Vue.use(Router)

const router = new Router({
  mode:'hash',
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
      path: '/Register', 
      component: Register,
      name: 'Register',
      meta:{title:'用户注册'}
    },
    {
      path: '/', 
      component: Home,
      name: 'Home',
      meta:{title:'金刚石文档编辑器'},
      redirect: '/welcome',
      children: [{path: '/welcome', component: Welcome}]
    },
    {
      path:'/Edit',
      component:Ue,
      name:'Edit',
      meta:{title:'无'}
    }
  ]

})

//路由导航守卫
/*router.beforeEach((to, from, next) => {
  if (to.path === '/login') return next();
  //获取token
  const tokenStr = window.sessionStorage.getItem('token')
  if (!tokenStr) return next('/login')
  next()
})*/

export default router
