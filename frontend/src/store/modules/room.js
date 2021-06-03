/*
 * @Description: 
 * @Author: l
 * @Date: 2021-06-03 13:45:26
 * @LastEditors: l
 * @LastEditTime: 2021-06-03 14:10:46
 * @FilePath: \DistributedControlSystem\frontend\src\store\modules\room.js
 */
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
    actions:{},
    modules:{},
    namespace:true,
}