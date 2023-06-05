import Vue from 'vue';
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
// import $ from 'jquery';

import App from './App.vue'

Vue.use(ElementUI);
// Vue.use($);

Vue.config.productionTip = false

new Vue({
    render: h => h(App),
}).$mount('#app')
