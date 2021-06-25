<!--
 * @Description: 
 * @Author: l
 * @Date: 2021-06-01 15:40:54
 * @LastEditors: l
 * @LastEditTime: 2021-06-25 22:27:15
 * @FilePath: \DistributedControlSystem\frontend\src\pages\Manager.vue
-->
<template>
  <div>
    <el-tabs :tab-position="tabPosition" style="height:1000px">
      <el-tab-pane label="获取报表">
        <div class="content">
          <div class="search-header">
            <el-row align="middle" type="flex">
              <el-col :span="6" :offset="2">
                <div class="grid-content">
                  <h4>请输入要查询的日期范围:</h4>
                </div>
              </el-col>
              <el-col :span="4" :offset="0" align="middle" type="flex">
                <el-date-picker
                  v-model="start2end"
                  type="daterange"
                  align="right"
                  unlink-panels
                  range-separator="至"
                  start-placeholder="开始日期"
                  end-placeholder="结束日期"
                  format="yyyy-MM-dd"
                  value-format="yyyy-MM-dd"
                  :picker-options="pickerOptions"
                >
                </el-date-picker>
              </el-col>
              <el-col :span="2" :offset="5" align="middle" type="flex">
                <div class="grid-content bg-purple-light">
                  <el-button
                    type="primary"
                    @click="checkReport({'startTime':start2end[0],'endTime':start2end[1]})"
                  >
                    获取报表report
                  </el-button>
                </div>
              </el-col>
              
            </el-row>
          </div>
          <div class="report-table">
            <el-table :data="report" border style="width: 100%" >
              <el-table-column prop="dateTime" label="date" width="130" >
              </el-table-column>
               <el-table-column prop="RDRNum" label="RDRNum" width="120" >
              </el-table-column>
              <el-table-column prop="commonSpeed" label="commonSpeed" width="130">
              </el-table-column>
              <el-table-column prop="commonTemp" label="commonTemp" width="130"> 
              </el-table-column>
              <el-table-column prop="satisfyNum" label="satisfyNum" width="130"> 
              </el-table-column>
              <el-table-column prop="scheduledNum" label="scheduledNum" width="130" >
              </el-table-column>
              <el-table-column prop="totalFee" label="totalFee" width="120" >
              </el-table-column>
              <el-table-column prop="totalNum" label="totalNum" width="120" >
              </el-table-column>
            </el-table>
          </div>
        </div>
      </el-tab-pane>
    </el-tabs>
  </div>
</template>

<script>
import { mapState, mapActions } from "vuex";
export default {
  data: function () {
    return {
      inputStartTime: '',
      inputEndTime: '',
      tabPosition: 'left',
      pickerOptions: {
          shortcuts: [{
            text: '最近一周',
            onClick(picker) {
              const end = new Date();
              const start = new Date();
              start.setTime(start.getTime() - 3600 * 1000 * 24 * 7);
              picker.$emit('pick', [start, end]);
            }
          }, {
            text: '最近一个月',
            onClick(picker) {
              const end = new Date();
              const start = new Date();
              start.setTime(start.getTime() - 3600 * 1000 * 24 * 30);
              picker.$emit('pick', [start, end]);
            }
          }, {
            text: '最近三个月',
            onClick(picker) {
              const end = new Date();
              const start = new Date();
              start.setTime(start.getTime() - 3600 * 1000 * 24 * 90);
              picker.$emit('pick', [start, end]);
            }
          }]
        },
      start2end: []
    };
  },
  computed: {
    ...mapState("manager", ["report", "reportIsOk", "startTime", "endTime"]),
  },
  methods: {
    ...mapActions("manager", ["checkReport"]),
    tryCheckReport:(start,end)=>{
      console.log("start2end:",start,end);
      this.checkReport({'startTime':start,'endTime':end})
    }
  },
  watch:{

  }
};
</script>

<style>
.report-div {
  background-color: white;
  margin-top: 50px;
  margin-right: 20%;
  margin-left: 20%;
}
.report-table{
  margin-top: 50px;
}
.content {
  margin-top: 50px;
  margin-left: 10%;
  margin-right: 10%;
  background-color: #fff;
}
</style>