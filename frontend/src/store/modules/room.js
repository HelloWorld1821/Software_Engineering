/*
 * @Description: 
 * @Author: l
 * @Date: 2021-06-03 13:45:26
 * @LastEditors: l
 * @LastEditTime: 2021-06-27 09:37:56
 * @FilePath: \DistributedControlSystem\frontend\src\store\modules\room.js
 */
const api = 'http://127.0.0.1:8000/room';
import axios from 'axios';
export default{
    state:{
        roomId:'',
        roomState:{
            speed:'',
            currTemp:'',
            targetTemp:'',
            fee:'',
            acState:''
        },
        roomParams:{
            tempSectionHigh:'',
            tempSectionLow:'',
            defaultTemp:'',
            defaultSpeed:'',
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
        updateRoomState({commit},payload){
            // console.log('updateRoomState...');
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
                    // console.log("changeRoomState fail..");
                } else {
                    ;
                }
            }).catch((error) => {
                console.error(error)
            });
        }
    },
    modules:{},
    namespaced:true,
}