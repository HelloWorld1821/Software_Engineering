<!--
 * @Description: 
 * @Author: l
 * @Date: 2021-06-01 10:29:38
 * @LastEditors: l
 * @LastEditTime: 2021-06-05 14:38:30
 * @FilePath: \DistributedControlSystem\frontend\src\pages\Login.vue
-->
<template>
<div>
    <h1>This is Login</h1>
    <div>Admin:<input type="text" value="admin" v-model="userName"></div>
    <div>Password:<input type="text" value="password" v-model="password"></div>
    <input type="button" value="LoginAdmin" @click="loginAdmin({userName,password})">
    <input type="button" value="Login" @click="login">
</div>
</template>

<script>
import { mapState, mapActions } from "vuex";
import { defineComponent } from '@vue/composition-api'

export default defineComponent({
    setup() {
        
    },
    name:'Login',
    data:function(){
        return{
            userName:"1",
            password:"password",
        }
    },
    methods:{
        // loginAdmin:function(userName,password){
        //     this.$store.dispatch("loginAdmin",{userName,password});
        //    // this.$store.dispatch("auth/loginAdmin",{userName,password});
        // }
        ...mapActions('auth',[
            'loginAdmin',
            'login'
        ])
    }
})
</script>
