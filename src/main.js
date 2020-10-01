import Vue from 'vue'
import VueRouter from 'vue-router'
import Vuex from 'vuex'

import routes from './routes'
import store from './store'

Vue.use(VueRouter)
Vue.use(Vuex)

Vue.config.productionTip = false

const router = new VueRouter({
  mode: 'history',
  routes,
  store
})

new Vue({
  router
}).$mount('#app')
