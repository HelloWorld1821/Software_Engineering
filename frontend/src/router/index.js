/*
 * @Description: 
 * @Author: l
 * @Date: 2021-05-31 13:38:16
 * @LastEditors: l
 * @LastEditTime: 2021-06-05 12:48:11
 * @FilePath: \DistributedControlSystem\frontend\src\router\index.js
 */
import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/pages/Home'
import Login from '@/pages/Login'
import Register from '@/pages/Register'
import Room from '@/pages/Room'
import Administrator from '@/pages/Administrator'
import Manager from '@/pages/Manager'
import Receptionist from '@/pages/Receptionist'
Vue.use(Router) // 让Vue安装VueRouter组件

//指定路由
export default new Router({
  routes: [
    {
      path: '/',
      redirect: '/home'
    },
    {
      path: '/home',
      name: 'home',
      component: Home
    },
    {
      path: '/login',
      name: 'login',
      component: Login
    },
    {
      path: '/register',
      name: 'register',
      component: Register
    },
    {
      path: '/room',
      name:'room',
      component:Room
    },
    {
      path:'/administrator',
      name:'administrator',
      component:Administrator
    },
    {
      path:'/manager',
      name:'manager',
      component:Manager
    },
    {
      path:'/receptionist',
      name:'receptionist',
      component:Receptionist
    }
  ]
})
