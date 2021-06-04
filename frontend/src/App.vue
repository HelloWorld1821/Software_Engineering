<!--
 * @Description: 
 * @Author: l
 * @Date: 2021-05-31 13:38:16
 * @LastEditors: l
 * @LastEditTime: 2021-06-04 12:30:46
 * @FilePath: \DistributedControlSystem\frontend\src\App.vue
-->
<template>
  <div id="app">
    <v-nav></v-nav>
    <router-view></router-view>
  </div>
</template>



<script>
import VNav from './components/VNav'
export default {
  name: "App",
  data(){
    return{
      msg:"aa",
      log_list:[]
    }
  },
  components:{
    VNav
  }
};
</script>

<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  /* -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale; */
  text-align: center;
  color: #2c3e50;
  background: url('assets/bg_1.jpg');
  background-size: 100% 100%; 
  /* background-color: pink; */
  height: 100%;
  width: 100%;
  position: fixed;
}
</style>
