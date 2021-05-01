import Vue from 'vue'
import App from './App.vue'
import router from './router'
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
import VueSmoothScroll from 'vue2-smooth-scroll'
import LoadScript from 'vue-plugin-load-script';

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

Vue.config.productionTip = false

Vue.use(BootstrapVue)
Vue.use(IconsPlugin)
Vue.use(VueSmoothScroll)
Vue.use(LoadScript);

new Vue({
  router,
  render: h => h(App),
}).$mount('#app')
