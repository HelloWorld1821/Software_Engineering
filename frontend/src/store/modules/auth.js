import axios from "axios";
import router from "../../router";

const api = "http://127.0.0.1:8000/user"; // 更新 API 地址

export default {
  state: {
    ds: true,
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
    setDs(state, ds) {
      state.ds = ds;
    },
    setLoading(state, loading) {
      state.loading = loading;
    },
    setError(state, error) {
      state.error = error;
    }
  },
  actions: {
    UserLogin({ commit, state }, payload) {
      console.log("UserLogin...");
      commit("setDs", false);
      commit("setLoading", true);
      commit("setUserName", payload.room_id); // 更新 userName 为 room_id
      commit("setPassword", payload.identity_card); // 更新 password 为 identity_card

      return axios
        .post(
          `${api}/login?room_id=${payload.room_id}&identity_card=${payload.identity_card}`
        )
        .then(response => {
          if (response.data.msg == "登录成功") {
            commit("setLoading", false);
            commit("setError", "");
            router.replace("/room");
          } else {
            commit("setLoading", false);
            commit("setError", "username or password error.");
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
