<!--
 * @Description: 
 * @Author: l
 * @Date: 2021-06-01 14:39:02
 * @LastEditors: l
 * @LastEditTime: 2021-06-04 00:17:18
 * @FilePath: \DistributedControlSystem\frontend\src\components\VNav.vue
-->
<template>
  <nav class="vnav">
    <div class="container">
      <a class="nav-brand">Distributed Control System</a>
      <div class='nav-collapse'>
      <ul class="menu">
        <li><router-link to="/home">home</router-link></li>
        <li><router-link to="/login">login</router-link></li>
        <li><router-link to="/register">register</router-link></li>
        <li><router-link to="/room">room</router-link></li>
        <li><router-link to="/administrator">administrator</router-link></li>
        <li><router-link to="/manager">manager</router-link></li>
        <li><router-link to="/receptionist">receptionist</router-link></li>
      </ul>
      </div>
    </div>
  </nav>
</template>

<script>
import { defineComponent } from "@vue/composition-api";

export default defineComponent({
  setup() {},
});
</script>
<style scoped>
* {
  list-style: none;
}
.vnav {
  font-family: "Work Sans", Arial, sans-serif;
  font-size: 12px;
  padding-bottom: 16px;
  padding-left: 16px;
  padding-right: 16px;
  padding-top: 16px;
  text-size-adjust: 100%;
  line-height: 28.8px;
  /* background-color: pink; */
  border-bottom-width: 10px;
  /* border-block-color: black; */
}
.nav-brand {
    -webkit-text-size-adjust: 100%;
    -webkit-tap-highlight-color: transparent;
    font-weight: 300;
    font-family: "Work Sans", Arial, sans-serif;
    -webkit-box-direction: normal;
    box-sizing: inherit;
    text-decoration: none;
    background-color: transparent;
    touch-action: manipulation;
    transition: .3s all ease;
    display: inline-block;
    padding-top: 0.3125rem;
    padding-bottom: 0.3125rem;
    font-size: 1.25rem;
    line-height: inherit;
    white-space: nowrap;
    text-transform: uppercase;
    letter-spacing: .1em;
    color: black;
}
.nav-collapse{
    -webkit-text-size-adjust: 100%;
    -webkit-tap-highlight-color: transparent;
    font-size: 1rem;
    font-weight: 300;
    line-height: 1.8;
    color: #868e96;
    font-family: "Work Sans", Arial, sans-serif;
    -webkit-box-direction: normal;
    box-sizing: inherit;
    flex-basis: 100%;
    -webkit-box-align: center;
    align-items: center;
    display: inline-block !important;
}
.menu {
  display: flex;
  box-sizing: border-box;
  flex-direction: row;
  margin-inline-start: 488.875px;
  margin-left: 488.875px;
}
.menu > ul > li {
  text-size-adjust: 100%;
  -webkit-text-size-adjust: 100%;
  -webkit-tap-highlight-color: transparent;
  font-size: 1rem;
  font-weight: 300;
  line-height: 1.8;
  color: #868e96;
  font-family: "Work Sans", Arial, sans-serif;
  list-style: none;
  -webkit-box-direction: normal;
  box-sizing: inherit;
}
.menu > li > a {
  -webkit-text-size-adjust: 100%;
  -webkit-tap-highlight-color: transparent;
  line-height: 1.8;
  font-family: "Work Sans", Arial, sans-serif;
  list-style: none;
  -webkit-box-direction: normal;
  box-sizing: inherit;
  text-decoration: none;
  background-color: transparent;
  touch-action: manipulation;
  transition: 0.3s all ease;
  display: block;
  padding: 1.6em 1em;
  font-size: 12px;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  font-weight: 400;
  color: black;
}
</style>
