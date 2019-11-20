import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const routes = [
    {
    path: '/faceAnalysis',
    name: 'faceAnalysis',
    component: () => import(/* webpackChunkName: "about" */ '../views/FaceAnalysisPage.vue')
  },
  {
    path: '/',
    name: 'main',
    component: () => import(/* webpackChunkName: "about" */ '../views/MainPage.vue')
  },
  {
    path: '/dictionary',
    name: 'dictionary',
    component: () => import(/* webpackChunkName: "about" */ '../views/DictionaryPage.vue')
  },
  {
    path: '/result',
    name: 'result',
    component: () => import(/* webpackChunkName: "about" */ '../views/AnalysisResultPage.vue')
  },
]

const router = new VueRouter({
  routes
})

export default router
