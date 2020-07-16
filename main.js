import Vue from 'vue'
import App from './App'

Vue.config.productionTip = false
Vue.prototype.$url = 'http://39.101.135.74:8000'
Vue.prototype.$photoUrl = 'http://39.101.135.74:8000/static/photo/'
App.mpType = 'app'

Vue.prototype.$note1 = ''
Vue.prototype.$note2 = ''

import store from './store'  


import cuCustom from './colorui/components/cu-custom.vue'
Vue.component('cu-custom',cuCustom)

const app = new Vue({
	store,
	...App
})
app.$mount()



