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
    <el-menu-item index="/login" route="/login">登录</el-menu-item>
    <el-menu-item index="/room" route="/room" :disabled="false"
      >用户</el-menu-item
    >
    <el-menu-item
      index="/administrator"
      route="/administrator"
      :disabled="false"
      >管理员</el-menu-item
    >
    <el-menu-item index="/receptionist" route="/receptionist" :disabled="false"
      >前台</el-menu-item
    >
    <el-menu-item index="/manager" route="/manager" :disabled="false"
      >经理</el-menu-item
    >
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
