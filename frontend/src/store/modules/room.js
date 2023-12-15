/*
 * @Description:
 * @Author: l
 * @Date: 2021-06-03 13:45:26
 * @LastEditors: l
 * @LastEditTime: 2021-06-27 09:37:56
 * @FilePath: \DistributedControlSystem\frontend\src\store\modules\room.js
 */
const api = '/api/schedule';
import axios from 'axios';
export default{
    state:{
        roomId: '114',
        roomState:{
            speed:'',
            currTemp:'',
            targetTemp:'',
            fee:'',
            acState:''
        },
        roomParams:{
            tempSectionHigh:'25',
            tempSectionLow:'18',
            defaultTemp: 20,
            defaultSpeed:'low',
            mode:'',
        }


    },
    getters:{},
    mutations:{
        setRoomId(state,roomId){
            state.roomId=roomId;
        },

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

        setTempSectionHigh(state,tempHigh){
            state.roomParams.tempSectionHigh=tempHigh;
        },
        setTempSectionLow(state,tempLow){
            state.roomParams.tempSectionLow=tempLow;
        },
        setDefaultTemp(state,defaultTemp){
            state.roomParams.defaultTemp=defaultTemp;
        },
        setDefaultSpeed(state,defaultSpeed){
            state.roomParams.defaultSpeed=defaultSpeed;
        },
        setMode(state,mode){
            state.roomParams.mode=mode;
        },
        setRoomParams(state,params){
            state.roomParams = params;
        }

    },
    actions:{
        // updateRoomState({commit},payload){
        //     // console.log('updateRoomState...');
        //     return axios.post(api + '/updateRoomState', {
        //         roomId:payload.roomId,
        //     }).then((response) => {
        //         if (response.data.error == false) {
        //             commit('setRoomState',response.data.roomState);
        //         } else {
        //             // commit('setRDRIsOk', false);
        //         }
        //     }).catch((error) => {
        //         console.error(error)
        //     });
        // },
        request_on({commit},payload){
            // console.log('updateRoomState...');
            // commit("setRoomId", payload.room_id);

            return axios.post(`${api}/request_on?room_id=${payload.room_id}`
            ).then((response) => {
                if (response.data.error == false) {
                    commit('setRoomState',response.data.roomState);
                } else {
                    // commit('setRDRIsOk', false);
                }
            }).catch((error) => {
                console.error(error)
            });
        },
        request_off({commit},payload){
            // console.log('updateRoomState...');
            // commit("setRoomId", payload.room_id);

            return axios.post(`${api}/request_off?room_id=${payload.room_id}`
            ).then((response) => {
                if (response.data.error == false) {
                    commit('setRoomState',response.data.roomState);
                } else {
                    // commit('setRDRIsOk', false);
                }
            }).catch((error) => {
                console.error(error)
            });
        },
        request_temp({commit},payload){
            // console.log('updateRoomState...');
            // commit("setRoomId", payload.room_id);
            commit("setTargetTemp", payload.target_temperature);

            return axios.post(`${api}/request_temp?room_id=${payload.room_id}&target_temperature=${payload.target_temperature}`
            ).then((response) => {
                if (response.data.error == false) {
                    commit('setRoomState',response.data.roomState);
                } else {
                    // commit('setRDRIsOk', false);
                }
            }).catch((error) => {
                console.error(error)
            });
        },
        request_speed({commit},payload){
            // console.log('updateRoomState...');
            // commit("setRoomId", payload.room_id);
            commit("setSpeed", payload.fan_speed);

            return axios.post(`${api}/request_speed?room_id=${payload.room_id}&fan_speed=${payload.fan_speed}`
            ).then((response) => {
                if (response.data.error == false) {
                    commit('setRoomState',response.data.roomState);
                } else {
                    // commit('setRDRIsOk', false);
                }
            }).catch((error) => {
                console.error(error)
            });
        },
        // changeRoomState({commit},payload){
        //     console.log('changeRoomState...');
        //     return axios.post(api + '/changeRoomState', {
        //         roomId:payload.roomId,
        //         targetTemp:payload.targetTemp,
        //         fan_speed:payload.fan_speed,
        //         acState:payload.targetACState,
        //     }).then((response) => {
        //         if (response.data.error == false) {
        //             // console.log("changeRoomState fail..");
        //         } else {
        //             ;
        //         }
        //     }).catch((error) => {
        //         console.error(error)
        //     });
        // }
    },
    modules:{},
    namespaced:true,
}
