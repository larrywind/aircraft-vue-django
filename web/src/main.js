// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import './static/style/index.css'
// 通用组件模块
import * as Packages from './packages/index'
// 数据模块
import lib from './static/libs/index'
// 配置AiagainUI模块
import comm from './components/index'

Vue.config.productionTip = false

Vue.use(Packages)

Vue.prototype.$api = lib.core
Vue.prototype.$util = lib.utils
Vue.prototype.$service = lib.service
Vue.prototype.$comm = comm

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
