<!--
 * @Description: 
 * @Author: l
 * @Date: 2021-06-01 14:39:02
 * @LastEditors: l
 * @LastEditTime: 2021-06-01 15:46:01
 * @FilePath: \client\src\components\VNav.vue
-->
<template>
  <div class='vnav'>
      <h2>This is VNav</h2>
        <router-link to='/home'>home</router-link>
        <router-link to='/login'>login</router-link>
        <router-link to='/register'>register</router-link>
        <router-link to='/room'>room</router-link>
        <router-link to='/administrator'>administrator</router-link>
        <router-link to='/manager'>manager</router-link>
        <router-link to='/receptionist'>receptionist</router-link>
        <br>
    <h1>-----------------------------------------------------------</h1>
  </div>
</template>

<script>
import { defineComponent } from '@vue/composition-api'

export default defineComponent({
    setup() {
        
    },
})
</script>
<style scoped>
.vnav
{
    background-color: pink;
}   
</style>