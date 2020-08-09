import Vue from 'vue'
import App from './App.vue'
import router from './router'
import axios from 'axios'
import VueAxios from 'vue-axios'
import ElementUI from 'element-ui';
import './assets/css/global.css'
import 'element-ui/lib/theme-chalk/index.css';

axios.defaults.baseURL = 'http://175.24.121.113:8000/myapp/register'
Vue.prototype.$http = axios

Vue.use(ElementUI);
Vue.use(VueAxios, axios)

Vue.config.productionTip = false

new Vue({
  render: h => h(App),
  router,
}).$mount('#app')
