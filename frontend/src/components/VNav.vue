<!--
 * @Description: 
 * @Author: l
 * @Date: 2021-06-01 14:39:02
 * @LastEditors: l
 * @LastEditTime: 2021-06-25 23:03:17
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
    :default-active="activeIndex"
    class="my-menu"
    mode="horizontal"
    router="true"
  >
    <el-menu-item index="1" route="/home">主页面</el-menu-item>
    <!-- <el-submenu index="2">
      <template slot="title">我的工作台</template>
      <el-menu-item index="2-1">选项1</el-menu-item>
      <el-menu-item index="2-2">选项2</el-menu-item>
      <el-menu-item index="2-3">选项3</el-menu-item>
      <el-submenu index="2-4">
        <template slot="title">选项4</template>
        <el-menu-item index="2-4-1">选项1</el-menu-item>
        <el-menu-item index="2-4-2">选项2</el-menu-item>
        <el-menu-item index="2-4-3">选项3</el-menu-item>
      </el-submenu>
    </el-submenu> -->
    <el-menu-item index="2" route="/login">登录</el-menu-item>
    <!-- <el-menu-item index="3" route="/register">注册</el-menu-item> -->
    <el-menu-item index="4" route="/room">用户</el-menu-item>
    <el-menu-item index="5" route="/administrator">管理员</el-menu-item>
    <el-menu-item index="6" route="/receptionist">前台</el-menu-item>
    <el-menu-item index="7" route="/manager">经理</el-menu-item>
  </el-menu>
</template>

<script>
import { defineComponent } from "@vue/composition-api";

export default defineComponent({
  setup() {},
});
</script>
<style scoped>
</style>
