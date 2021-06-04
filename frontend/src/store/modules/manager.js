/*
 * @Description: 
 * @Author: l
 * @Date: 2021-06-03 14:01:04
 * @LastEditors: l
 * @LastEditTime: 2021-06-04 14:07:19
 * @FilePath: \DistributedControlSystem\frontend\src\store\modules\manager.js
 */

const api = 'http://127.0.0.1:5000/manager';
import axios from 'axios'
export default{
    state:{
        startTime:'2021/6/4',
        endTime:'2021/6/5',
        reportIsOk:false,
        report:{
            totalNum: 20,
            commonTemp: 23,
            commonSpeed: 'mid',
            satisfyNum: 10,
            scheduledNum: 30,
            RDRNum: 25,
            totalFee: 10.0
        }
    },
    getter:{},
    mutations:{
        setReportIsOk(state,isOK){
            state.reportIsOk=isOK;
        },
        setStartTime(state,startTime){
            state.startTime=startTime;
        },
        setEndTime(state,endTime){
            state.endTime=endTime;
        },
        setReport(state,report){
            state.report.totalNum = report.totalNum;
            state.report.commonTemp=report.commonTemp;
            state.report.commonSpeed=report.commonSpeed;
            state.report.satisfyNum=report.satisfyNum;
            state.report.scheduledNum=report.scheduledNum;
            state.report.RDRNum=report.RDRNum;
            state.report.totalFee=report.totalFee;
        },
       
    },
    actions:{
    checkReport({commit,state},payload){
        console.log('checkReport...');
        return axios.post(api + '/checkReport',{
            startTime:payload.startTime,
            endTime:payload.endTime,
        }).then((response)=>{
            if(response.data.error == false){
                commit('setStartTime',payload.startTime);
                commit('setEndTime',payload.endTime);
                commit('setReportIsOk',true);
                commit('setReport',response.data.report);
            }else{
                commit('setReprotIsOk',false);
            }
        }).catch((error)=>{
            console.error(error)
        });
    }
    },
    modules:{},
    namespaced:true,
}