import RootView from './views/Root.vue'
import NotFoundView from './views/NotFound.vue'

export default [
  { path: '/', component: RootView },
  { path: '*', component: NotFoundView }
]