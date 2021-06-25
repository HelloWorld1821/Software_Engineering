/*
 * @Description: 
 * @Author: l
 * @Date: 2021-06-03 14:17:10
 * @LastEditors: l
 * @LastEditTime: 2021-06-26 00:31:57
 * @FilePath: \DistributedControlSystem\frontend\src\store\modules\administrator.js
 */
const api = '/api/administrator';
import axios from 'axios'
export default{
    state:{
        roomsState:[],
        stateIsOk:false,
    },
    getter:{},
    mutations:{
        setRoomsState(state,roomsState){
            // console.log('111');
            state.roomsState=roomsState;
        },
        setStateIsOk(state,isOk){
            state.stateIsOk=isOk;
        }
    },
    actions:{
        checkRoomsState({commit}){
            console.log('checkRoomsState...');
            return axios.post(api + '/checkRoomsState', {
            }).then((response) => {
                // console.log(response.data);
                if (response.data.error == false) {
                    // console.log('---');
                    commit('setRoomsState',response.data.roomsState);
                    commit('setStateIsOk', true);
                } else {
                    commit('setStateIsOk', false);
                }
            }).catch((error) => {
                console.error(error);
            });
        },
        setDefaultParams({commit},payload){
            console.log('setDefaultParams...');
            return axios.post(api + '/setDefaultParams', {
                // mode:'cold',
                // tempSection:[10,15,20,25],
                // defaultTemp:20,
                // feeRate:1.5,
                // scheduledNum:3
                payload
            }).then((response) => {
                if (response.data.error == false) {
                    console.log('setDefaultParams succeed');
                } else {
                    // commit('setStateIsOk', false);
                    console.log('setDefaultParams fail');
                }
            }).catch((error) => {
                console.error(error);
            });
        }
    },
    modules:{},
    namespaced:true,
}