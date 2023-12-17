<template>
  <div>
    <div class="background"></div>
    <div class="container">
      <!-- 登录框 -->
      <h1>管理员登录</h1>
      <el-form label-width="70px" size="small" class="login-form">
        <el-row type="flex" style="justify-content: center;margin-top: 20px ">
          <h2>账号登录</h2>
        </el-row>
        <el-row type="flex" class="input-row" style="margin-top: 10px" >
          <el-col :span="6"> 密码: </el-col>
          <el-col :span="10">
            <el-input v-model="password" show-password placeholder="请输入您的密码" style=" width: 200px"></el-input>
          </el-col>
        </el-row>
        <el-button
          class="login-button"
          type="primary"
          @click="AdminLogin({ room_id, password })"
          >登录</el-button
        >
      </el-form>
    </div>
  </div>
</template>

<script>
import { mapState, mapActions } from "vuex";
import { defineComponent } from "@vue/composition-api";

export default defineComponent({
  setup() {},
  name: "AdminLogin",
  data: function() {
    return {
      password: "",
      imgSrc: require("../assets/images/room.jpg")
    };
  },
  methods: {
    ...mapActions("administrator", ["AdminLogin"]),
    reset: function() {
      console.log("reset");
      this.room_id = "";
      this.password = "";
    },
  }
});
</script>
<style scoped>
  .background {
    background-color: rgba(194, 205, 220, 0.5);
    top: 0px;
    width: 100%;
    height: 100%;
    z-index: -1;
    position: absolute;
  }
  
  .container {
    display: flex;
    flex-direction: column;
    justify-content: center; /* 垂直居中 */
    align-items: center; /* 水平居中 */
  }

  h1{
    margin-bottom: 20px;
  }

  .login-form {
    background-color: rgb(64, 91, 131, 0.8);
    color: white;
    justify-content: center;
    /* border-radius: 10px; */
    box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
    /* background-color: rgba(255, 255, 255, 0.8); */
  }

.input-row{
  margin-right:120px;
  margin-left: 80px;
}

  
  .login-button {
    margin-top: 30px;
    background-color: #1f3045;
    border-color: #1f3045;
    font-size: 18px;
    width: 30%;
    margin-bottom: 40px;
  }
</style>