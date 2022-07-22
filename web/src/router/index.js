import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

export default new Router({
  // mode:'history',
  routes: [
    // main page
    {path: '/', name:'', component: resolve => require(['../views/index'],resolve)},
  ]
})
