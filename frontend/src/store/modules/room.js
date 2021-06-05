/*
 * @Description: 
 * @Author: l
 * @Date: 2021-06-03 13:45:26
 * @LastEditors: l
 * @LastEditTime: 2021-06-05 13:24:06
 * @FilePath: \DistributedControlSystem\frontend\src\store\modules\room.js
 */
const api = 'http://127.0.0.1:5000/room';
import axios from 'axios';
export default{
    state:{
        roomId:10,
        roomState:{
            speed:'low',
            currTemp:25,
            targetTemp:26,
            fee:0.0,
            acState:'on'
        }
    },
    getters:{},
    mutations:{
        setSpeed(state,speed){
            state.roomState.speed = speed;
        },
        setCurrTemp(state,currTemp){
            state.roomState.currTemp=currTemp;
        },
        setTargetTemp(state,targetTemp){
            state.roomState.targetTemp=targetTemp;
        },
        setFee(state,fee){
            state.roomState.fee=fee;
        },
        setAcState(state,acState){
            state.roomState.acState=acState;
        },
        setRoomState(state,roomState){
            state.roomState=roomState;
        },
        setRoomId(state,roomId){
            state.roomId=roomId;
        }
    },
    actions:{
        updateRoomState({commit},payload){
            console.log('updateRoomState...');
            return axios.post(api + '/updateRoomState', {
                roomId:payload.roomId,
            }).then((response) => {
                if (response.data.error == false) {
                    commit('setRoomState',response.data.roomState);
                } else {
                    // commit('setRDRIsOk', false);
                }
            }).catch((error) => {
                console.error(error)
            });
        },
        changeRoomState({commit},payload){
            console.log('changeRoomState...');
            return axios.post(api + '/changeRoomState', {
                roomId:payload.roomId,
                targetTemp:payload.targetTemp,
                targetSpeed:payload.targetSpeed,
                acState:payload.targetACState,
            }).then((response) => {
                if (response.data.error == false) {
                    // commit('setRoomState',response.data.roomState);
                } else {
                    // commit('setRDRIsOk', false);
                }
            }).catch((error) => {
                console.error(error)
            });
        }
    },
    modules:{},
    namespaced:true,
}