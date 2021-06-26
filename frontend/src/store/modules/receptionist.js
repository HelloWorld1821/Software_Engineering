/*
 * @Description: 
 * @Author: l
 * @Date: 2021-06-03 14:12:06
 * @LastEditors: l
 * @LastEditTime: 2021-06-26 16:44:45
 * @FilePath: \DistributedControlSystem\frontend\src\store\modules\receptionist.js
 */
const api = '/api/receptionist';
import axios from 'axios';
export default{
    state:{
        billRoomId:'',
        RDRRoomId:'',
        billIsOk:false,
        RDRIsOk:false,
        RDR:[
        ],
        bill:''
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