import Vue from 'vue'
import App from './App'

Vue.config.productionTip = false
Vue.prototype.$url = 'http://192.168.0.100:4444'
App.mpType = 'app'



import cuCustom from './colorui/components/cu-custom.vue'
Vue.component('cu-custom',cuCustom)

const app = new Vue({
	...App
})
app.$mount()


