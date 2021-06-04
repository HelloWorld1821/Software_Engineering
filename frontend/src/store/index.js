/*
 * @Description: 
 * @Author: l
 * @Date: 2021-06-01 17:15:19
 * @LastEditors: l
 * @LastEditTime: 2021-06-04 13:15:03
 * @FilePath: \DistributedControlSystem\frontend\src\store\index.js
 */
import Vue from 'vue';
import Vuex from 'vuex';
import auth from './modules/auth'
import manager from './modules/manager'
Vue.use(Vuex);

export default new Vuex.Store({
    
    modules:{
        auth,
        manager,
    }
})