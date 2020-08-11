import Vue from 'vue'
import Router from 'vue-router'
import Login from './components/user/login.vue'
import Register from './components/user/register.vue'
import FindPassword from './components/user/FindPassword.vue'
import User from './components/user/UserInfo.vue'
import Home from './components/user/home.vue'
import Welcome from './components/user/welcome.vue'
import Ue from './components/edit/ue.vue'
import Recently from './components/user/recently.vue'
import Myproduction from './components/user/myproduction.vue'
import Favorite from './components/user/favorite.vue'
import Trashbin from './components/user/trashbin.vue'


Vue.use(Router)

const router = new Router({
  routes: [
    {
      path: '/changeInfo', 
      component: User, 
      name:'ChangeInfo',
      meta:{title:'修改密码及个人信息'}
    },
    {
      path: '/Login', 
      component: Login,
      name: 'Login',
      meta:{title:'金刚石文档编辑器'}
    },
    {
      path: '/Register', 
      component: Register,
      name: 'Register',
      meta:{title:'用户注册'}
    },
    {
      path:'/FindPassword',
      component:FindPassword,
      name:'FindPassword',
      meta:{title:'找回密码'}
    },
    
    {
      path: '/', 
      component: Home,
      name: 'Home',
      meta:{title:'金刚石文档编辑器'},
      redirect: '/welcome',
      children: [
        {path: '/welcome', component: Welcome,meta:{title:'金刚石文档编辑器'}},
        {path: '/recently', component: Recently},
        {path: '/myproduction', component: Myproduction},
        {path: '/favorite', component: Favorite},
        {path: '/trashbin', component: Trashbin}
      ]
    },
    {
      path:'/Edit',
      component:Ue,
      name:'Edit',
      meta:{title:'无'}
    }
  ],
  mode:"history"
})

//路由导航守卫
/*router.beforeEach((to, from, next) => {
  if (to.path === '/login' || to.path === '/Register' || to.path === '/welcome' || to.path === '/') return next();
  //获取token
  const tokenStr = window.sessionStorage.getItem('token')
  if (!tokenStr) return next('/login')
  next()
})*/

export default router
