import Vue from "vue";
import Router from "vue-router";
import Home from "@/pages/Home";
import Login from "@/pages/Login";
import AdminLogin from "@/pages/AdminLogin";
import Register from "@/pages/Register";
import Room from "@/pages/Room";
import Administrator from "@/pages/Administrator";

import Receptionist from "@/pages/Receptionist";
Vue.use(Router); // 让Vue安装VueRouter组件

//指定路由
export default new Router({
  routes: [
    {
      path: "/",
      redirect: "/home"
    },
    {
      path: "/home",
      name: "home",
      component: Home
    },
    {
      path: "/login",
      name: "login",
      component: Login
    },
    {
      path: "/adminlogin",
      name: "adminlogin",
      component: AdminLogin
    },
    {
      path: "/register",
      name: "register",
      component: Register
    },
    {
      path: "/room",
      name: "room",
      component: Room
    },
    {
      path: "/administrator",
      name: "administrator",
      component: Administrator
    },

    {
      path: "/receptionist",
      name: "receptionist",
      component: Receptionist
    }
  ]
});
