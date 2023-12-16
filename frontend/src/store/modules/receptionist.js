/*
 * @Description:
 * @Author: l
 * @Date: 2021-06-03 14:12:06
 * @LastEditors: l
 * @LastEditTime: 2021-06-26 16:44:45
 * @FilePath: \DistributedControlSystem\frontend\src\store\modules\receptionist.js
 */
const api = "/api/admin"; //修改后端接口
import axios from "axios";
export default {
  state: {
    room_id: "",
    billRoomId: "",
    RDRRoomId: "",
    billIsOk: false,
    RDRIsOk: false,
    RDR: [],
    totalCost: 0
  },
  getter: {},
  mutations: {
    setBillRoomId(state, room_id) {
      state.room_id = room_id;
    }, //从
    // setUserName(state, room_id) {
    //     state.room_id = room_id;
    //   },
    setRDRRoomId(state, RDRRoomId) {
      state.RDRRoomId = RDRRoomId;
    },
    setRDR(state, RDR) {
      state.RDR = RDR;
    },
    setTotalCost(state, total_cost) {
      state.totalCost = total_cost;
    },
    setBillIsOk(state, isOk) {
      state.billIsOk = isOk;
    },
    setRDRIsOk(state, isOk) {
      state.RDRIsOk = isOk;
    }
  },

  // return axios
  // .post(
  //   `${api}/login?room_id=${payload.room_id}&identity_card=${payload.identity_card}`
  // )
  // .then(response => {

  actions: {
    getRDR({ commit }, payload) {
      console.log("getRDR...");
      return axios
        .get(`${api}/records/${payload.roomId}`)
        .then(response => {
          commit("setRDR", response.data);
          commit("setRDRIsOk", true);
          commit("setRDRRoomId", payload.roomId);
        })
        .catch(error => {
          console.error(error);
        });
    },
    getBill({ commit }, payload) {
      console.log("getBill...");
      // commit('setBillRoomId',payload.room_id);
      return axios
        .get(`${api}/bills/${payload.room_id}`)
        .then(response => {
          commit("setTotalCost", response.data.total_cost);
          commit("setBillIsOk", true);
          console.log("Updated totalCost:", response.data.total_cost); // 记录状态
          commit("setBillRoomId", payload.room_id);
        })
        .catch(error => {
          console.error(error);
        });
    },

    DeleteRoom({ commit }, payload) {
      console.log("DeleteRoom...");
      // commit('setBillRoomId',payload.room_id);
      return axios
        .delete(`${api}/delete?room_id=${payload.room_id}`)
        .then(response => {
          if (response.data.error == false) {
            commit("setdelete", response.data.bill);
            commit("setdeleteIsOk", true);
            commit("setdeleteRoomId", payload.room_id);
          } else {
            commit("setdeleteIsOk", false);
          }
        })
        .catch(error => {
          console.error(error);
        });
    },

    CreateRoom({ commit }, payload) {
      console.log("CreateRoom...");
      // commit('setBillRoomId',payload.room_id);
      commit("setLoading", true);
      commit("setroom_id", payload.room_id); // 更新 userName 为 room_id
      commit("setidentity_card", payload.identity_card); // 更新 password 为 identity_card
      commit("setinitial_temperature", payload.initial_temperature);

      return axios
        .post(
          `${api}/create?room_id=${payload.room_id}&identity_card=${payload.identity_card}&initial_temperature=${payload.initial_temperature}`,
          {
            room_id: payload.room_id,
            identity_card: payload.identity_card,
            initial_temperature: payload.initial_temperature
          }
        )

        .then(response => {
          // Handle the successful response here
          // 处理成功的响应
          console.log("Success:", response.data);
          // 这里可以进行进一步操作，比如更新状态或跳转到另一个页面
        })
        .catch(error => {
          // Handle the error response here
          // 处理错误的响应
          if (error.response) {
            // API请求已发出并且服务器响应了状态码
            // 服务器响应的状态码不在2xx的范围内
            if (error.response.status === 422) {
              // 处理验证错误
              let errorDetails = error.response.data.detail;
              errorDetails.forEach(err => {
                console.log(`Validation error at ${err.loc}: ${err.msg}`);
                // 根据需要进行更多处理，例如设置表单字段的验证状态或显示错误消息
              });
            } else {
              // 处理其他类型的API错误
              console.error("API error:", error.response);
            }
          } else if (error.request) {
            // 请求已发出，但没有收到响应
            // `error.request`在浏览器中是 XMLHttpRequest 的实例
            // 而在node.js中是 http.ClientRequest 的实例
            console.error("No response received:", error.request);
          } else {
            // 发送请求时出了点问题
            console.error("Error:", error.message);
          }
        });
    }
  },
  modules: {},
  namespaced: true
};
