<!--
 * @Description: 
 * @Author: l
 * @Date: 2021-05-31 13:38:16
 * @LastEditors: l
 * @LastEditTime: 2021-06-01 15:01:44
 * @FilePath: \client\src\App.vue
-->
<template>
  <div id="app">
    <v-nav></v-nav>
    <!-- <img src="./assets/logo.png" /> -->
    
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
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
