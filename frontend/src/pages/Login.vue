<!--
 * @Description: 
 * @Author: l
 * @Date: 2021-06-01 10:29:38
 * @LastEditors: l
 * @LastEditTime: 2021-06-26 21:38:24
 * @FilePath: \DistributedControlSystem\frontend\src\pages\Login.vue
-->
<template>
  <div>
    <div class="background">
      <img :src="imgSrc" width="100%" height="100%" alt="" />
    </div>
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
      <!-- <el-form-item label="用户名">
        <el-input v-model="userName"></el-input>
      </el-form-item> -->
      <el-row align="middle" type="margin-top: 20px">
        <el-col :span="10"> 账号: </el-col>
        <el-col :span="10">
          <el-autocomplete
            class="inline-input"
            v-model="userName"
            :fetch-suggestions="querySearch"
            placeholder="请输入账号"
          ></el-autocomplete>
        </el-col>
      </el-row>
      <el-row align="middle" type="flex" style="margin-top: 20px">
        <el-col :span="10"> 密码: </el-col>
        <el-col :span="10">
          <el-input
            v-model="password"
            show-password
            placeholder="请输入密码"
          ></el-input>
        </el-col>
      </el-row>
      <el-row align="middle" type="flex" style="margin-top: 20px">
        <el-col :span="8" :offset="3">
          <el-button type="primary" @click="loginAdmin({ userName, password })">
            登录
          </el-button>
        </el-col>
        <el-col :span="10">
          <el-button @click="reset">重置</el-button>
        </el-col>
      </el-row>
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
      userList: [
        { value: "room_1" },
        { value: "room_2" },
        { value: "room_3" },
        { value: "room_4" },
        { value: "receptionist_1" },
        { value: "manager_1" },
        { value: "administrator_1" },
      ],
      userName: "",
      password: "",
      imgSrc: require("../assets/images/room.jpg"),
    };
  },
  computed: {
    ...mapState("auth", ["role"]),
  },
  watch: {
    // role: function () {
    //   console.log("current role:", this.role);
    //   switch (this.role) {
    //     case "room":
    //       this.$router.replace("/room");
    //       break;
    //     case "administrator":
    //       this.$router.replace("/administrator");
    //       break;
    //     case "manager":
    //       this.$router.replace("/manager");
    //       break;
    //     case "receptionist":
    //       this.$router.replace("/receptionist");
    //       break;
    //     default:
    //       console.log("illegal role");
    //       this.$router.replace("/home");
    //       break;
    //   }
  },
  methods: {
    ...mapActions("auth", ["loginAdmin"]),
    reset: function () {
      console.log("reset");
      this.userName = "";
      this.password = "";
    },
    querySearch(queryString, cb) {
      var userList = this.userList;
      var results = queryString
        ? userList.filter(this.createFilter(queryString))
        : userList;
      // 调用 callback 返回建议列表的数据
      cb(results);
    },
  },
});
</script>
<style scoped>
.background {
  top :0px; ;
  width: 100%;
  height: 100%; /**宽高100%是为了图片铺满屏幕 */
  z-index: -1;
  position: absolute;
}

.login-form {
  margin-top:10%;
  margin-right: 35%;
  margin-left: 35%;

  border-radius: 30px;
  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
  padding-top: 30px;
  padding-left: 40px;
  padding-right: 40px;
  padding-bottom: 25px;
  background-color: rgba(255, 255, 255, 0.8);



 
}
</style>