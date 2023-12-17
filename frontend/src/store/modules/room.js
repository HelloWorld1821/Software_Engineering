const api = "/api/schedule";
import axios from "axios";
export default {
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
      tempSectionHigh: "25",
      tempSectionLow: "18",
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
    setRoomId(state, roomId) {
      state.roomId = roomId;
    },
    setStatus(state, status) {
      state.adminStatus = status;
    },
    setSpeed(state, speed) {
      state.roomState.speed = speed;
    },
    setCurrTemp(state, currTemp) {
      state.roomState.currTemp = currTemp;
    },
    setTargetTemp(state, targetTemp) {
      state.roomState.targetTemp = targetTemp;
    },
    setFee(state, fee) {
      state.roomState.fee = fee;
    },
    setAcState(state, acState) {
      state.roomState.acState = acState;
    },
    setRoomState(state, roomState) {
      state.roomState = roomState;
    },

    setTempSectionHigh(state, tempHigh) {
      state.roomParams.tempSectionHigh = tempHigh;
    },
    setTempSectionLow(state, tempLow) {
      state.roomParams.tempSectionLow = tempLow;
    },
    setRoomState1(state, showState) {
      state.showState = showState;
    },
    setDefaultTemp(state, defaultTemp) {
      state.roomParams.defaultTemp = defaultTemp;
    },
    setDefaultSpeed(state, defaultSpeed) {
      state.roomParams.defaultSpeed = defaultSpeed;
    },
    setMode(state, mode) {
      state.roomParams.mode = mode;
    },
    setRoomParams(state, params) {
      state.roomParams = params;
    }
  },
  actions: {
    request_on({ commit }, payload) {
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
    request_off({ commit }, payload) {
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
    async showRoomState1({ commit }, payload) {
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

    async showRoomState({ commit }, payload) {
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
    request_temp({ commit }, payload) {
      // console.log('updateRoomState...');
      // commit("setRoomId", payload.room_id);
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
    request_speed({ commit }, payload) {
      // console.log('updateRoomState...');
      // commit("setRoomId", payload.room_id);
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
    // changeRoomState({commit},payload){
    //     console.log('changeRoomState...');
    //     return axios.post(api + '/changeRoomState', {
    //         roomId:payload.roomId,
    //         targetTemp:payload.targetTemp,
    //         fan_speed:payload.fan_speed,
    //         acState:payload.targetACState,
    //     }).then((response) => {
    //         if (response.data.error == false) {
    //             // console.log("changeRoomState fail..");
    //         } else {
    //             ;
    //         }
    //     }).catch((error) => {
    //         console.error(error)
    //     });
    // }
  },
  modules: {},
  namespaced: true
};
