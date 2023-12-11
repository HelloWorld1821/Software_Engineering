<!--
 * @Description:
 * @Author: l
 * @Date: 2021-06-01 15:40:54
 * @LastEditors: l
 * @LastEditTime: 2021-06-27 01:01:03
 * @FilePath: \DistributedControlSystem\frontend\src\pages\Manager.vue
-->
<template>
  <div>
    <el-tabs :type="border - card" style="height:500px">
      <el-tab-pane>
        <template slot="label">
          <div class="label" style="color:rgb(226, 183, 43);">
            <h2>获取报表</h2>
          </div>
        </template>
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
                    round
                    @click="
                      checkReport({
                        startTime: start2end[0],
                        endTime: start2end[1]
                      })
                    "
                  >
                    获取报表
                  </el-button>
                </div>
              </el-col>
            </el-row>
          </div>
          <div class="report-table">
            <el-table :data="report" border style="width: 100%">
              <el-table-column
                sortable
                prop="dateTime"
                label="date"
                width="163"
              >
              </el-table-column>
              <el-table-column
                sortable
                prop="RDRNum"
                label="RDRNum"
                width="163"
              >
              </el-table-column>
              <el-table-column
                sortable
                prop="commonSpeed"
                label="commonSpeed"
                width="163"
              >
              </el-table-column>
              <el-table-column
                sortable
                prop="commonTemp"
                label="commonTemp"
                width="163"
              >
              </el-table-column>
              <el-table-column
                sortable
                prop="satisfyNum"
                label="satisfyNum"
                width="163"
              >
              </el-table-column>
              <el-table-column
                sortable
                prop="scheduledNum"
                label="scheduledNum"
                width="163"
              >
              </el-table-column>
              <!-- <el-table-column prop="totalFee" label="totalFee" width="143" >
              </el-table-column> -->
              <el-table-column
                sortable
                prop="totalNum"
                label="totalNum"
                width=""
              >
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
  data: function() {
    return {
      inputStartTime: "",
      inputEndTime: "",
      tabPosition: "left",
      imgSrc: require("../assets/images/room.jpg"),
      pickerOptions: {
        shortcuts: [
          {
            text: "最近一周",
            onClick(picker) {
              const end = new Date();
              const start = new Date();
              start.setTime(start.getTime() - 3600 * 1000 * 24 * 7);
              picker.$emit("pick", [start, end]);
            }
          },
          {
            text: "最近一个月",
            onClick(picker) {
              const end = new Date();
              const start = new Date();
              start.setTime(start.getTime() - 3600 * 1000 * 24 * 30);
              picker.$emit("pick", [start, end]);
            }
          },
          {
            text: "最近三个月",
            onClick(picker) {
              const end = new Date();
              const start = new Date();
              start.setTime(start.getTime() - 3600 * 1000 * 24 * 90);
              picker.$emit("pick", [start, end]);
            }
          }
        ]
      },
      start2end: []
    };
  },
  computed: {
    ...mapState("manager", ["report", "reportIsOk", "startTime", "endTime"])
  },
  methods: {
    ...mapActions("manager", ["checkReport"]),
    tryCheckReport: (start, end) => {
      console.log("start2end:", start, end);
      this.checkReport({ startTime: start, endTime: end });
    }
  },
  watch: {}
};
</script>

<style scoped>
.report-div {
  background-color: rgba(255, 255, 255, 0.932);
  margin-top: 50px;
  margin-right: 20%;
  margin-left: 20%;
}
.report-table {
  margin-top: 50px;
  background-color: rgba(93, 93, 93, 0.5);

  border-radius: 30px;
}
.content {
  margin-top: 20px;
  margin-left: 5%;
  margin-right: 5%;
  border-radius: 30px;

  backdrop-filter: blur(10px);
  background: linear-gradient(rgba(255, 255, 255, 0.1), rgba(0, 0, 0, 0.5));

  box-shadow: 0 20px 40px 1px rgba(0, 0, 0, 0.12);

  height: 500px;
}
.background {
  width: 100%;
  height: 100%; /**宽高100%是为了图片铺满屏幕 */
  z-index: -1;
  position: absolute;
}
.label {
  margin-top: -5px;
}
</style>
<style>
.el-tabs__item {
  margin-top: 0px;
  margin-left: 10px;
  margin-right: 10px;
  margin-bottom: 15px;
}
.el-tabs__nav-scroll {
  backdrop-filter: blur(15px);
  background: linear-gradient(rgba(255, 255, 255, 0.1), rgba(0, 0, 0, 0.3));
  box-shadow: 0 20px 40px 3px rgba(0, 0, 0, 0.253);
}
</style>
