<!--
 * @Description: 
 * @Author: l
 * @Date: 2021-06-01 10:29:38
 * @LastEditors: l
 * @LastEditTime: 2021-06-14 14:44:51
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
    computed:{
        ...mapState('auth',[
            'role'
        ]),
        
    },
    watch:{
        role:function(){
            console.log('current role:',this.role);
            switch(this.role){
                        case 'room':
                            this.$router.replace('/room');
                            break;
                        case 'administrator':
                            this.$router.replace('/administrator');
                            break;
                        case 'manager':
                            this.$router.replace('/manager');
                            break;
                        case 'receptionist':
                            this.$router.replace('/receptionist');
                            break;
                        default:
                            console.log('illegal role');
                            this.$router.replace('/home');
                            break;
                    }
        }
    },
    methods:{
        ...mapActions('auth',[
            'loginAdmin',
            'login'
        ])
    }
})
</script>
