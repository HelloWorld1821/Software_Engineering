<!--
 * @Description: 
 * @Author: l
 * @Date: 2021-06-01 10:29:38
 * @LastEditors: l
 * @LastEditTime: 2021-06-14 15:09:17
 * @FilePath: \DistributedControlSystem\frontend\src\pages\Login.vue
-->
<template>
  <div>
    <!-- <h1>This is Login</h1>
    <div>Admin:<input type="text" value="admin" v-model="userName" /></div>
    <div>
      Password:<input type="text" value="password" v-model="password" />
    </div>
    <input
      type="button"
      value="LoginAdmin"
      @click="loginAdmin({ userName, password })"
    />
    <input type="button" value="Login" @click="login" /> -->

    <form action="" method="post" class="smart-green">
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
    </form>
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
      userName: "1",
      password: "password",
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
    ...mapActions("auth", ["loginAdmin", "login"]),
  },
});
</script>
<style scoped>
.smart-green {
  margin-left: auto;
  margin-right: auto;
  max-width: 500px;
  background: #f8f8f8;
  padding: 30px 30px 20px 30px;
  font: 12px Arial, Helvetica, sans-serif;
  font-family: "Work Sans", Arial, sans-serif;
  color: #666;
  border-radius: 5px;
}
.smart-green h1 {
  font: 24px "Trebuchet MS", Arial, Helvetica, sans-serif;
  font-family: "Work Sans", Arial, sans-serif;
  padding: 20px 40px 20px 40px;
  display: block;
  margin: -30px -30px 10px -30px;
  color: #fff;
  background: #9dc45f;
  text-shadow: 1px 1px 1px #949494;
  border-radius: 5px 5px 0px 0px;
  border-bottom: 1px solid #89af4c;
}
.smart-green h1 > span {
  display: block;
  font-size: 11px;
  color: #fff;
}

.smart-green label {
  display: block;
  margin: 0px 0px 5px;
}
.smart-green label > span {
  float: left;
  margin-top: 10px;
  color: #5e5e5e;
}
.smart-green input[type="text"] {
  color: #555;
  height: 30px;
  line-height: 15px;
  width: 100%;
  padding: 0px 0px 0px 10px;
  margin-top: 2px;
  border: 1px solid #e5e5e5;
  background: #fbfbfb;
  outline: 0;
  box-shadow: inset 1px 1px 2px rgba(238, 238, 238, 0.2);
  font: normal 14px/14px Arial, Helvetica, sans-serif;
}

.smart-green .button {
  background-color: #9dc45f;
  border-radius: 5px;
  border: none;
  padding: 10px 25px 10px 25px;
  color: #fff;
  text-shadow: 1px 1px 1px #949494;
}
.smart-green .button:hover {
  background-color: #80a24a;
}
</style>
