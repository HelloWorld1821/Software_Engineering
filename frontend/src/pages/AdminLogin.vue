<template>
  <div>
    <div class="background"></div>
    <div class="header">
      <div class="left-section">
        <h1>波普特廉价酒店|空调管理系统</h1>
      </div>
    </div>
    <!-- 主体 -->
    <div class="container">
      <!-- 登录框 -->
      <div class="right-form">
        <el-form label-width="70px" size="small" class="login-form">
          <el-row type="flex" style="justify-content: center;margin-top: 20px ">
            <h2>账号登录</h2>
          </el-row>
          <el-row type="flex" style="margin-top: 40px;margin-bottom: 10px">
          </el-row>
          <el-row type="flex" style="margin-top: 20px">
            <el-col :span="6" class="login-text"> 密码: </el-col>
            <el-col :span="10">
              <el-input
                v-model="password"
                show-password
                placeholder="请输入您的密码"
                style=" width: 200px"
              ></el-input>
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

.header {
  margin-top: 2.5%;
  display: flex;
}

.bottom {
  margin-top: 2.5%;
  display: flex;
}

.left-section {
  flex: 3;
  display: flex;
  justify-content: left;
  align-items: flex-start;
  margin-left: 10%;
  margin-bottom: 1%;
}
.right-section {
  flex: 2;
  display: flex;
  justify-content: left;
  align-items: flex-start;
}

.container {
  display: flex;
  height: 100vh;
  align-items: stretch;
}

.left-image {
  flex: 3;
  display: flex;
  justify-content: right;
  align-items: flex-start;
  margin-bottom: 10%;
}

.left-image image {
  width: 25%;
  height: auto; /* 高度自动调整 */
  object-fit: contain;
  margin-left: 5%;
}

.right-form {
  flex: 2;
  display: flex;
  justify-content: left;
  align-items: flex-start;
  margin-bottom: 10%;
  margin-left: 5%;
}

.login-form {
  background-color: rgb(64, 91, 131, 0.8);
  color: white;
  right: 10%;
  height: 70%;
  width: 60%;
  /* border-radius: 10px; */
  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
  /* background-color: rgba(255, 255, 255, 0.8); */
}

.login-button {
  margin-top: 40px;
  background-color: #1f3045;
  border-color: #1f3045;
  font-size: 18px;
  width: 30%;
}
</style>
