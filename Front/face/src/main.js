import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify';
import router from './router'
import store from './store'
import InfiniteScroll from 'v-infinite-scroll'

Vue.config.productionTip = false
Vue.use(InfiniteScroll)

new Vue({
  vuetify,
  router,
  store,
  render: h => h(App)
}).$mount('#app')
