/*
 * @Description: 
 * @Author: l
 * @Date: 2021-06-03 14:12:06
 * @LastEditors: l
 * @LastEditTime: 2021-06-04 15:18:23
 * @FilePath: \DistributedControlSystem\frontend\src\store\modules\receptionist.js
 */
const api = 'http://127.0.0.1:5000/receptionist';
import axios from 'axios'
export default{
    state:{
        billRoomId:10,
        RDRRoomId:9,
        billIsOk:false,
        RDRIsOk:false,
        RDR:{
            startTime: '2021-6-2,15:20',
            endTime: '2021-6-3,16:40',
            speed: 'high',
            fee: 2333.3,
        },
        bill:{
            fee:10.0,
        }
    },
    getter:{},
    mutations:{
        setBillRoomId(state,billRoomId){
            state.billRoomId=billRoomId;
        },
        setRDRRoomId(state,RDRRoomId){
            state.RDRRoomId=RDRRoomId;
        },
        setRDR(state,RDR){
            state.RDR=RDR;
        },
        setBill(state,bill){
            state.bill=bill;
        },
        setBillIsOk(state,isOk){
            state.billIsOk=isOk;
        },
        setRDRIsOk(state,isOk){
            state.RDRIsOk=isOk;
        }
    },
    actions:{
        getRDR({commit},payload){
            console.log('getRDR...');
            return axios.post(api + '/getRDR', {
                roomId:payload.roomId,
            }).then((response) => {
                if (response.data.error == false) {
                    commit('setRDR', response.data.RDR);
                    commit('setRDRIsOk', true);
                    commit('setRDRRoomId',payload.roomId);
                } else {
                    commit('setRDRIsOk', false);
                }
            }).catch((error) => {
                console.error(error)
            });
        },
        getBill({commit},payload){
            console.log('getBill...');
            return axios.post(api + '/getBill', {
                roomId:payload.roomId,
            }).then((response) => {
                if (response.data.error == false) {
                    commit('setBill', response.data.bill);
                    commit('setBillIsOk', true);
                    commit('setBillRoomId',payload.roomId);
                } else {
                    commit('setBillIsOk', false);
                }
            }).catch((error) => {
                console.error(error)
            });
        }
    },
    modules:{},
    namespaced:true,
}