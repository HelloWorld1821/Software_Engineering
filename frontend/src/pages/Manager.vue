<!--
 * @Description: 
 * @Author: l
 * @Date: 2021-06-01 15:40:54
 * @LastEditors: l
 * @LastEditTime: 2021-06-04 14:15:58
 * @FilePath: \DistributedControlSystem\frontend\src\pages\Manager.vue
-->
<template>
  <div>
      <h2>Manager</h2>
      StartTime:
      <input type='text' v-model="inputStartTime" >
      <br>
      EndTime:
      <input type ='text' v-model="inputEndTime">
      <br>
      <input type="button" value='get report' @click="checkReport({startTime:inputStartTime,endTime:inputEndTime})">
      reportIsOk:{{reportIsOk}}
      <div v-if='reportIsOk==true'>
        <div class="report-div">
        Report:
        <template>
          <p>开始时间startTime:{{startTime}}</p>
          <p>结束时间endTime:{{endTime}}</p>
          <p>使用空调次数totalNum:{{report.totalNum}}</p>
          <p>最常使用的温度commonTemp:{{report.commonTemp}}</p>
          <p>最常使用的风速commonSpeed:{{report.commonSpeed}}</p>
          <p>到达目标温度的次数satisfyNum:{{report.satisfyNum}}</p>
          <p>被调度的次数scheduledNum:{{report.scheduledNum}}</p>
          <p>生成RDR的次数RDRNum:{{report.RDRNum}}</p>
          <p>总费用totalFee:{{report.totalFee}}</p>
        </template>
        </div>
      </div>
      <div v-else>Sorry,we can't show the report ,the reportIsOk is false</div>
  </div>
</template>

<script>
import { mapState, mapActions } from "vuex";
export default {
  data:function(){
      return {
        inputStartTime:'2021/2/1',
        inputEndTime:'2021/2/4',
      }
  },
  computed:{
    ...mapState('manager',[
      'report',
      'reportIsOk',
      'startTime',
      'endTime',
    ])
  },
  methods:{
    ...mapActions('manager',[
      'checkReport',
    ])
  }
  
}
</script>

<style>
.report-div{
  background-color: white;
  margin-top: 50px;
  margin-right: 20%;
  margin-left: 20%;
}
</style>