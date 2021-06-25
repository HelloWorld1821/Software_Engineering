<!--
 * @Description: 
 * @Author: l
 * @Date: 2021-06-01 10:29:38
 * @LastEditors: l
 * @LastEditTime: 2021-06-25 18:26:41
 * @FilePath: \DistributedControlSystem\frontend\src\pages\Login.vue
-->
<template>
  <div>
    <!-- <form action="" method="post" claspxs="smart-green">

      <h1>Login</h1>
      <label>
        <span>Your User Name :</span>
        <input
          id="username"
          type="text"
          name="username"
          placeholder="Your User Name"
          v-model="userName"
        />
      </label>
      <label>
        <span>Your Password :</span>
        <input
          id="password"
          type="text"
          name="password"
          placeholder="Your Password"
          v-model="password"
        />
      </label>
      <label>
        <span>&nbsp;</span>
        <input
          type="button"
          class="button"
          value="Login"
          @click="loginAdmin({ userName, password })"
        />
      </label>
    </form> -->
    <el-form label-width="60px" size="small" class="login-form">
      <el-form-item label="用户名">
        <el-input v-model="userName"></el-input>
      </el-form-item>
      <el-form-item label="密码">
        <el-input v-model="password"></el-input>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="loginAdmin({ userName, password })">
          登录
        </el-button>
        <el-button @click="reset">重置</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
import { mapState, mapActions } from "vuex";
import { defineComponent } from "@vue/composition-api";

export default defineComponent({
  setup() {},
  name: "Login",
  data: function () {
    return {
      userName: "",
      password: "",
    };
  },
  computed: {
    ...mapState("auth", ["role"]),
  },
  watch: {
    role: function () {
      console.log("current role:", this.role);
      switch (this.role) {
        case "room":
          this.$router.replace("/room");
          break;
        case "administrator":
          this.$router.replace("/administrator");
          break;
        case "manager":
          this.$router.replace("/manager");
          break;
        case "receptionist":
          this.$router.replace("/receptionist");
          break;
        default:
          console.log("illegal role");
          this.$router.replace("/home");
          break;
      }
    },
  },
  methods: {
    ...mapActions("auth", ["loginAdmin"]),
    reset: function(){
      console.log('reset');
      this.userName="";
      this.password="";
    },
  },
});
</script>
<style scoped>
.login-form {
  margin-right: 35%;
  margin-left: 35%;
  margin-top: 50px;
}
</style>