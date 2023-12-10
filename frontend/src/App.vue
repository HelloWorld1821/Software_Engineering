<!--
 * @Description:
 * @Author: l
 * @Date: 2021-05-31 13:38:16
 * @LastEditors: l
 * @LastEditTime: 2021-06-26 21:45:23
 * @FilePath: \DistributedControlSystem\frontend\src\App.vue
-->
<template>
  <div id="app">
    <v-nav></v-nav>
    <router-view v-if="isRouterAlive"></router-view>
  </div>
</template>

<script>
import VNav from "./components/VNav";
export default {
  name: "App",
  provide() {
    return {
      reload: this.reload
    };
  },
  data() {
    return {
      isRouterAlive: true
    };
  },
  methods: {
    reload() {
      this.isRouterAlive = false;
      this.$nextTick(function() {
        this.isRouterAlive = true;
      });
    }
  },
  components: {
    VNav
  }
};
</script>

<style>
@import "./assets/css/font_face.css";
* {
  font-family: "meet";
}
#app {
  font-family: "meet";
  /* -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale; */
  text-align: center;
  color: #2c3e50;
  /* background: url('assets/bg_1.jpg'); */
  /* background-size: 100% 100%;  */
  /* background-color: pink; */
  height: 100%;
  width: 100%;
  position: fixed;
  background: url("../src/assets/images/room.jpg");
}
body {
  margin: 0;
}
</style>
