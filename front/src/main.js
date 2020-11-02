import Vue from "vue";
import VueRouter from "vue-router";
import Vuex from "vuex";
import VueNativeSock from "vue-native-websocket";

import routes from "./routes";
import store from "./store";

Vue.use(VueRouter);
Vue.use(Vuex);
Vue.use(VueNativeSock);

Vue.config.productionTip = false;

const router = new VueRouter({
  mode: "history",
  routes,
});

new Vue({
  router,
  store,
}).$mount("#app");
