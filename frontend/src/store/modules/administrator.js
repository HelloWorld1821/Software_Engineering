import router from "../../router";
const api = "http://127.0.0.1:8000/admin"; // 更新 API 地址
import axios from "axios";
export default {
  state: {
    roomsState: [],
    stateIsOk: false,
    isDisabled: true
  },
  getter: {},
  mutations: {
    setPassword(state, password) {
      state.password = password;
    },
    setRoomsState(state, roomsState) {
      state.roomsState = roomsState;
    },
    setStateIsOk(state, isOk) {
      state.stateIsOk = isOk;
    },
    setLoginIsOk(state, isOk) {
      state.isDisabled = isOk;
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
          if (response.data.msg == "登录成功") {
            commit("setError", "");
            commit("setLoginIsOk", false);
            const menuItems = ["/administrator", "/receptionist", "/manager"];

            menuItems.forEach(item => {
              const menuItem = document.querySelector(`[index="${item}"]`);
              if (menuItem) {
                menuItem.setAttribute("disabled", "false");
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
        .finally(() => {
          commit("setLoading", false);
        });
    },
    async checkRoomsState({ commit }) {
      try {
        console.log("checkRoomsState...");
        const response = await axios.get(api + "/rooms");
        if (Array.isArray(response.data) && response.data.length > 0) {
          commit("setRoomsState", response.data);
          commit("setStateIsOk", true);
        } else {
          commit("setStateIsOk", false);
        }
      } catch (error) {
        console.error(error);
      }
    },
    // ...（其他 action 保持不变）

    setDefaultParams({ commit }, payload) {
      console.log("setDefaultParams...");
      let p = payload;
      const queryParams = new URLSearchParams({
        room_id: p.roomId,
        target_temperatuer: p.target_Temp,
        fan_speed: p.fanSpeed,
        status: p.Status
      });

      return axios
        .post(`${api}/modify?${queryParams}`)
        .then(response => {
          if (response.data.error === false) {
            console.log("setDefaultParams succeed");
          } else {
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
