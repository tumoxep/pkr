import RootView from "./views/Root.vue";
import RegisterView from "./views/Register.vue";
import LoginView from "./views/Login.vue";
import NotFoundView from "./views/NotFound.vue";

export default [
  { path: "/", component: RootView },
  { path: "/register", component: RegisterView },
  { path: "/login", component: LoginView },
  { path: "*", component: NotFoundView },
];
