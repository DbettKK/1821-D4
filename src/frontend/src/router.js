import Vue from 'vue'
import Router from 'vue-router'
import Login from './components/user/login.vue'
import ChangeInfo from './components/user/userInfo.vue'
import Home from './components/user/home.vue'
import Welcome from './components/user/welcome.vue'
import NotFoundComponent from './components/NotFoundComponent.vue'

Vue.use(Router)

const router = new Router({
  routes: [
    {
      path: '/changeInfo', 
      component: ChangeInfo, 
      name:'ChangeInfo',
      meta:{title:'修改密码及个人信息'}
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
      children: [{path: '/welcome', component: Welcome,meta:{title:'金刚石文档编辑器'}}]
    },
    {
      path:'*',
      component:NotFoundComponent,
      meta:{title:'页面未找到'}
    }
  ],
  mode:"history"
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
