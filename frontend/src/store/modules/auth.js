/*
 * @Description: 
 * @Author: l
 * @Date: 2021-06-02 15:34:01
 * @LastEditors: l
 * @LastEditTime: 2021-06-16 19:08:11
 * @FilePath: \DistributedControlSystem\frontend\src\store\modules\auth.js
 */
// const api = 'http://10.28.174.15:5000/auth';
const api = '/api/auth';
import axios from 'axios'

export default{
    state:{
        roomId:'',
        userName:'',
        password:'',
        loading:false,
        error:'',
        role:'home',
    },
    getter:{},
    mutations:{     
        setRoomId(state,roomId){
            state.roomId = roomId;
        },
        setUserName(state,userName){
            state.userName = userName;
        },
        setPassword(state,password){
            state.password = password;
        },
        setLoading(state,loading){
            state.loading = loading;
        },
        setError(state,error){
            state.error = error;
        },
        setRole(state,role){
            state.role=role;
        }
    },
    actions:{
        // login(context){
        //     context.commit("xxx")
        // }
        loginAdmin({commit,state},payload){
            console.log("loginAdmin...");
            
            commit('setLoading',true);//显示正在加载中
            commit('setUserName',payload.userName);//更新userName
            commit('setPassword',payload.password);//更新password
            let that = this;
            return axios.post(api + '/loginAdmin',{
                userName:state.userName,
                password:state.password,
            }).then((resposne)=>{
                if(resposne.data.error == true){
                    commit('setLoading',false);//取消加载
                    commit('setError','username or password error.');//加载错误
                }else{
                    commit('setLoading',false);
                    commit('setError','');
                    commit('setRole',resposne.data.role);
                }
            }).catch((error)=>{
                console.error(error)
            });
        },
        login({commit,state},payload){
            console.log("login...");
            return axios.get('/apid').then((resposne)=>{
                // if(resposne.data.error == true){
                //     commit('setLoading',false);//取消加载
                //     commit('setError','username or password error.');//加载错误
                // }else{
                //     commit('setLoading',false);
                //     commit('setError','');
                // }
                console.log(resposne)
            }).catch((error)=>{
                console.error(error)
            });
        }
    },
    modules:{},
    namespaced:true
}