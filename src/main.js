import Vue from 'vue'
import App from './App.vue'
import router from './router'
import Vuex from 'vuex'
import axios from 'axios'
import VueAxios from 'vue-axios'
import ElementUI from 'element-ui';
//import { quillEditor } from 'vue-quill-editor'
//import * as Quill from 'quill';

import './assets/css/global.css'
import 'element-ui/lib/theme-chalk/index.css';
//import 'quill/dist/quill.core.css'
//import 'quill/dist/quill.snow.css'
//import 'quill/dist/quill.bubble.css'
import qs from 'qs';

axios.defaults.baseURL = 'http://175.24.121.113:8000/myapp/register'
//axios请求拦截
axios.interceptors.request.use(config => {
  console.log (config)
  config.headers.Authorization = window.sessionStorage.getItem('token')
  return config
})
Vue.prototype.$http = axios
Vue.prototype.$qs = qs;

Vue.use(ElementUI);
Vue.use(VueAxios, axios)
Vue.use(Vuex)
//Vue.use(VueQuillEditor, /* { default global options } */)

Vue.config.productionTip = false

const store =new Vuex.Store({
  state:{
    token:''
  },
  mutations:{
    exit(state){
      state.token=''
    },
    login(state,new_token){
      state.token=new_token
    }
  }
})

new Vue({
  store:store,
  render: h => h(App),
  router,
}).$mount('#app')

