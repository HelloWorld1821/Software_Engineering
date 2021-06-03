/*
 * @Description: 
 * @Author: l
 * @Date: 2021-06-03 14:01:04
 * @LastEditors: l
 * @LastEditTime: 2021-06-03 14:11:49
 * @FilePath: \DistributedControlSystem\frontend\src\store\modules\manager.js
 */
export default{
    state:{
        report:{
            totalNum: 20,
            commonTemp: 23,
            commonSpeed: 'mid',
            satisfyNum: 10,
            scheduledNum: 30,
            RDRNum: 25,
            totalFee: 12450.0
        }
    },
    getter:{},
    mutations:{
        setReport(state,report){
            state.totalNum = report.totalNum;
            state.commonTemp=report.commonTemp;
            state.commonSpeed=report.commonSpeed;
            state.satisfyNum=report.satisfyNum;
            state.scheduledNum=report.scheduledNum;
            state.RDRNum=report.RDRNum;
            state.totalFee=report.totalFee;
        }
    },
    actions:{},
    modules:{},
    namespace:true,
}