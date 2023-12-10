<!--
 * @Description: 
 * @Author: l
 * @Date: 2021-06-01 14:39:02
 * @LastEditors: l
 * @LastEditTime: 2021-06-27 00:15:02
 * @FilePath: \DistributedControlSystem\frontend\src\components\VNav.vue
-->
<template>
  <!-- <nav class="vnav">
    <div class="container">
      <a class="nav-brand">Distributed Control System</a>
      <div class='nav-collapse'>
      <ul class="menu">
        <li><router-link to="/home">home</router-link></li>
        <li><router-link to="/login">login</router-link></li>
        <li><router-link to="/register">register</router-link></li>
        <li><router-link to="/room">room</router-link></li>
        <li><router-link to="/administrator">administrator</router-link></li>
        <li><router-link to="/manager">manager</router-link></li>
        <li><router-link to="/receptionist">receptionist</router-link></li>
      </ul>
      </div>
    </div>
  </nav> -->

  <el-menu
    :default-active="$route.path"
    class="my-menu"
    mode="horizontal"
    router
    background-color="#545c64"
    text-color="#fff"
    active-text-color="#ffd04b"
  >
    <el-menu-item index="/home" route="/home">主页面</el-menu-item>
    <el-menu-item index="/login" route="/login">登录</el-menu-item>
    <!-- <el-menu-item index="3" route="/register">注册</el-menu-item> -->
    <el-menu-item index="/room" route="/room" :disabled="false">用户</el-menu-item>
    <el-menu-item index="/administrator" route="/administrator" :disabled="false">管理员</el-menu-item>
    <el-menu-item index="/receptionist" route="/receptionist" :disabled="false">前台</el-menu-item>
    <el-menu-item index="/manager" route="/manager" :disabled="false">经理</el-menu-item>
  </el-menu>
</template>

<script>
import { defineComponent } from "@vue/composition-api";
import router from '../router';
export default defineComponent({
  
  setup() {},
});
</script>
<style scoped>
</style>
