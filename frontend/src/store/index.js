import Vue from "vue";
import Vuex from "vuex";
import auth from "./modules/auth";

import receptionist from "./modules/receptionist";
import administrator from "./modules/administrator";
import room from "./modules/room";
Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    auth,

    receptionist,
    administrator,
    room
  }
});
