/*
 * @Description:
 * @Author: l
 * @Date: 2021-06-03 14:17:10
 * @LastEditors: l
 * @LastEditTime: 2021-06-27 01:39:18
 * @FilePath: \DistributedControlSystem\frontend\src\store\modules\administrator.js
 */
import router from "../../router";
const api = "http://127.0.0.1:8000/admin";
import axios from "axios";
export default {
  state: {
    roomsState: [],
    stateIsOk: false
  },
  getter: {},
  mutations: {
    setPassword(state, password) {
      state.password = password;
    },
    setRoomsState(state, roomsState) {
      // console.log('111');
      state.roomsState = roomsState;
    },
    setStateIsOk(state, isOk) {
      state.stateIsOk = isOk;
    }
  },
  actions: {
    AdminLogin({ commit, state }, payload) {
      console.log("AdminLogin...");
      commit("setLoading", true);
      // commit("setPassword", payload.password); // 更新 password

      return axios
        .post(`${api}/login?password=${payload.password}`)
        .then(response => {
          if (response.data.msg=="登录成功") {
            commit("setError", "");
           
            const menuItems = [
              '/administrator',
              '/receptionist',
              '/manager'
            ];
    
            menuItems.forEach(item => {
              const menuItem = document.querySelector(`[index="${item}"]`);
              if (menuItem) {
                menuItem.setAttribute('disabled', 'false');
              }
            });

            router.replace("/administrator");
          } else {
            commit("setError", "password error.");
          }
        })
        .catch(error => {
          console.error(error);
        })
        .finally(()=>{
          commit("setLoading",false);
        })
    },
    checkRoomsState({ commit }) {
      console.log("checkRoomsState...");
      return axios
        // .get(api + "/rooms")
        .get('/admin/rooms')
        .then(response => {
          if (response.data.error === false) {
            commit("setRoomsState", response.data.roomsState);
            commit("setStateIsOk", true);
          } else {
            commit("setStateIsOk", false);
          }
        })
        .catch(error => {
          console.error(error);
        });
    },

    setDefaultParams({ commit }, payload) {
      console.log("setDefaultParams...");
      let p = payload;
      return axios
        .post(api + "/setDefaultParams", {
          // mode:'cold',
          // tempSection:[10,15,20,25],
          // defaultTemp:20,
          // feeRate:1.5,
          // scheduledNum:3
          defaultMode: p.defaultMode,
          defaultTemp: p.defaultTemp,
          defaultSpeed: p.defaultSpeed,
          feeRate: p.feeRate,
          scheduledNum: p.scheduledNum,
          coldHigh: p.coldHigh,
          coldLow: p.coldLow,
          hotHigh: p.hotHigh,
          hotLow: p.hotLow
        })
        .then(response => {
          if (response.data.error == false) {
            console.log("setDefaultParams succeed");
          } else {
            // commit('setStateIsOk', false);
            console.log("setDefaultParams fail");
          }
        })
        .catch(error => {
          console.error(error);
        });
    }
  },
  modules: {},
  namespaced: true
};
