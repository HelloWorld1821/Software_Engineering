/*
 * @Description: 
 * @Author: l
 * @Date: 2021-06-01 17:15:19
 * @LastEditors: l
 * @LastEditTime: 2021-06-02 16:38:06
 * @FilePath: \frontend\src\store\index.js
 */
import Vue from 'vue';
import Vuex from 'vuex';
import auth from './modules/auth'
Vue.use(Vuex);

export default new Vuex.Store({
    
    modules:{
        auth
    }
})