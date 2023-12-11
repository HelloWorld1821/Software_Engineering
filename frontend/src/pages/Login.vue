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
    </div> 
    <div class="header">
      <div class="left-section">
        <h1 >波普特廉价酒店|空调管理系统</h1>
      </div>
      <div class="right-section"></div>
    </div>
    <div class="container">
      <div class="left-image">
        <img :src="imgSrc" height="70%" alt="left_image" />
      </div> 
      <div class="right-form">
        <el-form label-width="70px" size="small" class="login-form">
          <!-- <el-form-item label="用户名">
            <el-input v-model="userName"></el-input>
          </el-form-item> -->
          <h3>账号登录</h3>
          <el-row align="middle" type="margin-top: 20px">
            <el-col :span="10"> 账号: </el-col>
            <el-col :span="10">
              <el-autocomplete class="inline-input" v-model="userName":fetch-suggestions="querySearch" placeholder="请输入您的账号"
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
      
    </div>
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
  background-color: rgb(194, 220, 220);
  top :0px; ;
  width: 100%;
  height: 100%; /**宽高100%是为了图片铺满屏幕 */
  z-index: -1;
  position: absolute;
}

.header{
  margin-top: 2.5%;
  display: flex;
}

.left-section{
  flex: 3;
  display: flex;
  justify-content: left;
  align-items:flex-start;
  margin-left: 10%;
  margin-bottom: 1%;
}
.right-section{
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

.left-image{
  flex: 3;
  display: flex;
  justify-content: right;
  align-items:flex-start;
  margin-bottom: 10%;

}

.left-image image{
  width: 25%; /* 图片的最大宽度为容器宽度 */
  height: auto; /* 高度自动调整 */
  object-fit: contain; /* 保持图片内容在框架内且不失真 */
  margin-left: 5%;
}

.right-form{
  flex: 2;
  display: flex;
  justify-content: left;
  align-items: flex-start;
  margin-bottom: 10%;
  margin-left: 5%;
}

.login-form {
  /* position: absolute; */
  right: 10%;
  height: 70%;
  width: 60%;
  border-radius: 10px;
  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
  background-color: rgba(255, 255, 255, 0.8);
}
</style>