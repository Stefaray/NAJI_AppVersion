import Vue from 'vue'
import App from './App'

Vue.config.productionTip = false
Vue.prototype.$url = 'http://172.30.57.70:4444'
Vue.prototype.$photoUrl = 'http://172.30.57.70:4444/static/photo/'
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



