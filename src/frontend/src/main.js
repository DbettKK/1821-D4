import Vue from 'vue'
import App from './App.vue'
import router from './router'
import Vuex from 'vuex'
import axios from 'axios'
import VueAxios from 'vue-axios'
import ElementUI from 'element-ui';
import './assets/css/global.css'
import 'element-ui/lib/theme-chalk/index.css';
import qs from 'qs';

axios.defaults.baseURL = 'http://175.24.121.113:8000/myapp/register'
Vue.prototype.$http = axios
Vue.prototype.$qs = qs;

Vue.use(ElementUI);
Vue.use(VueAxios, axios)
Vue.use(Vuex)

Vue.config.productionTip = false

const store =new Vuex.Store({
  state:{
    token:'123456'
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

