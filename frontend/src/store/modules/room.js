const api = "/api/schedule";
import axios from "axios";

export default {//房间参数的一些默认值，在快速调试时可以使用
  state: {
    roomId: "114",
    room_id: "114",
    roomState: {
      speed: "",
      currTemp: "",
      targetTemp: "",
      fee: "",
      acState: ""
    },
    roomParams: {
      tempSectionHigh: "35",
      tempSectionLow: "15",
      defaultTemp: 20,
      defaultSpeed: "low",
      mode: ""
    },
    showState: [],
    adminStatus: [
      {
        record_id: 18,
        room_id: 2,
        initial_temperature: 28,
        total_cost: 4,
        identity_card: "1",
        current_temperature: 25,
        target_temperature: 25,
        fan_speed: "medium",
        status: "SLEEPING",
        server_time: 0
      }
    ]
  },
  getters: {},
  mutations: {
    setStatus(state, status) {
      state.adminStatus = status;
    },
    setSpeed(state, speed) {
      state.roomState.speed = speed;
    },
    setTargetTemp(state, targetTemp) {
      state.roomState.targetTemp = targetTemp;
    },
    setRoomState(state, roomState) {
      state.roomState = roomState;
    },
    setRoomState1(state, showState) {
      state.showState = showState;
    },
  },
  actions: {
    request_on({commit}, payload) {//调用api接口，返回给后端空调开启信息
      return axios
        .post(`${api}/request_on?room_id=${payload.room_id}`)
        .then(response => {
          if (response.data.error == false) {
            commit("setRoomState", response.data.roomState);
          } else {
          }
        })
        .catch(error => {
          console.error(error);
        });
    },
    request_off({commit}, payload) {//调用api接口，返回给后端空调关闭信息
      return axios
        .post(`${api}/request_off?room_id=${payload.room_id}`)
        .then(response => {
          if (response.data.error == false) {
            commit("setRoomState", response.data.roomState);
          } else {
          }
        })
        .catch(error => {
          console.error(error);
        });
    },
    async showRoomState1({commit}, payload) {//调用从后端获取get信息，通过setStatus将get信息传到前端，以显示在用户控制面板中
      try {
        console.log("checkRoomsState, room_id:", payload.room_id);
        const response = await axios.get(`/api/user/show/${payload.room_id}`);
        commit("setRoomState1", response.data);
      } catch (error) {
        console.error(error);
      }
      try {
        const response = await axios.get(
          `/api/admin/rooms/?room_id=${payload.room_id}`
        );
        commit("setStatus", response.data[0]);
      } catch (error) {
        console.error(error);
      }
    },

    async showRoomState({commit}, payload) {
      try {
        console.log("checkRoomsState...");
        const response = await axios.get(`/user/show/${payload.room_id}`);
        if (Array.isArray(response.data) && response.data.length > 0) {
          commit("setRoomsState1", response.data);
          commit("setStateIsOk", true);
        } else {
          commit("setStateIsOk", false);
        }
      } catch (error) {
        console.error(error);
      }
    },
    request_temp({commit}, payload) {//调用api接口，返回给后端温度信息
      commit("setTargetTemp", payload.target_temperature);

      return axios
        .post(
          `${api}/request_temp?room_id=${payload.room_id}&target_temperature=${payload.target_temperature}`
        )
        .then(response => {
          if (response.data.error == false) {
            commit("setRoomState", response.data.roomState);
          } else {
            // commit('setRDRIsOk', false);
          }
        })
        .catch(error => {
          console.error(error);
        });
    },
    request_speed({commit}, payload) {//调用api接口，返回给后端风速信息
      commit("setSpeed", payload.fan_speed);

      return axios
        .post(
          `${api}/request_speed?room_id=${payload.room_id}&fan_speed=${payload.fan_speed}`
        )
        .then(response => {
          if (response.data.error == false) {
            commit("setRoomState", response.data.roomState);
          } else {
            // commit('setRDRIsOk', false);
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
