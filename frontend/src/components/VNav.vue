<!--
 * @FilePath: \DistributedControlSystem\frontend\src\components\VNav.vue
-->
<template>
  <el-menu
    :default-active="$route.path"
    class="menu"
    mode="horizontal"
    router
    text-color="white"
  >
    <el-menu-item index="/login" route="/login">用户登录</el-menu-item>
    <el-menu-item index="/adminlogin" route="/adminlogin">管理员登录</el-menu-item>
    <el-menu-item index="/room" route="/room" :disabled="true">房间</el-menu-item>
    <el-menu-item index="/administrator"route="/administrator":disabled="true">管理员</el-menu-item>
    <el-menu-item index="/receptionist" route="/receptionist" :disabled="true">前台</el-menu-item>
    <el-menu-item index="/manager" route="/manager" :disabled="true">经理</el-menu-item>
  </el-menu>
</template>

<script>
import { defineComponent } from "@vue/composition-api";
import router from "../router";
export default defineComponent({
  setup() {}
});
</script>


<style scoped>
.menu {
  background-color: #486589;
}

.menu .el-menu-item {
  font-size: 16px;
}

.menu .el-menu-item:not(.is-disabled):hover {
  color: #0b1525;
}

.menu .el-menu-item.is-active {
  font-weight: bold;
  color: #182f54;
  background-color: white;
}
</style>
