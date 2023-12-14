import axios from "axios";
import router from "../../router";

const api = "http://127.0.0.1:8000/user"; // 更新 API 地址

export default {
  state: {
    room_id: "",
    identity_card: "",
    loading: false,
    error: "",
    role: "home"
  },
  mutations: {
    setUserName(state, room_id) {
      state.room_id = room_id;
    },
    setPassword(state, identity_card) {
      state.identity_card = identity_card;
    },
    setLoading(state, loading) {
      state.loading = loading;
    },
    setError(state, error) {
      state.error = error;
    },
    setRole(state, role) {
      state.role = role;
    }
  },
  actions: {
    UserLogin({ commit, state }, payload) {
      console.log("UserLogin...");

      commit("setLoading", true);
      commit("setUserName", payload.room_id); // 更新 userName 为 room_id
      commit("setPassword", payload.identity_card); // 更新 password 为 identity_card

      return axios
        .post(
          `${api}/login?room_id=${payload.room_id}&identity_card=${payload.identity_card}`
        )
        .then(response => {
          if (response.data.error) {
            commit("setLoading", false);
            commit("setError", "username or password error.");
          } else {
            commit("setLoading", false);
            commit("setError", "");
            commit("setRole", response.data.role);

            switch (response.data.role) {
              case "room":
                router.replace("/room");
                break;
              case "administrator":
                router.replace("/administrator");
                break;
              case "manager":
                router.replace("/manager");
                break;
              case "receptionist":
                router.replace("/receptionist");
                break;
              default:
                console.log("illegal role");
                router.replace("/home");
                break;
            }
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
