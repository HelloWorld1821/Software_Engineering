<!--
 * @Description: 
 * @Author: l
 * @Date: 2021-06-01 15:36:52
 * @LastEditors: l
 * @LastEditTime: 2021-06-26 17:47:40
 * @FilePath: \DistributedControlSystem\frontend\src\pages\Administrator.vue
-->
<template>
  <div>
    <!-- <h2>Admistrator</h2>
    <div class="rooms-state-div">
      <input
        type="button"
        value="get the rooms' state"
        @click="checkRoomsState"
      />
      <template v-if="stateIsOk">
        <br>
        Rooms'State:
        <div
          v-for="(roomState, i) in roomsState"
          v-bind:key="i"
          class="room-state"
        >
          第{{ i+1 }}个房间:
          roomId:{{ roomState.roomState.roomId }}
          isCheckIn:{{roomState.roomState.isCheckIn}}
          currTemp:{{ roomState.roomState.currTemp }}
          targetTemp:{{ roomState.roomState.targetTemp }}
          speed:{{ roomState.roomState.speed }}
          mode:{{ roomState.roomState.mode }}
        </div>
      </template>
    </div>
    <div class="default-params-set-div">
      <br>
      <input type="button" value="set defualt params" @click="setDefaultParams">

    </div> -->

    <el-tabs :tab-position="tabPosition" style="height: 1000px">
      <!-- 管理员监视面板 -->
      <el-tab-pane label="监视房间">
        <div class="content">
          <div class="rooms-table">
            <el-table :data="roomsState" border style="width: 100%">

              <el-table-column label="房间ID" width="143">
                <template slot-scope="scope">
                  <i class="el-icon-user"></i>
                  {{scope.row.roomId}}
                </template>
              </el-table-column>

              <el-table-column label="送风状态" width="143">
                <template slot-scope="scope">
                  <!-- {{ scope.row.state }} -->
                  <el-switch
                    :disabled="true"
                    v-model="scope.row.state"
                    active-color="#13ce66"
                    inactive-color="#ff4949"
                    active-value="sending"
                    inactive-value="not sending"
                  >
                  </el-switch>
                </template>
              </el-table-column>
              <el-table-column prop="mode" label="空调模式" width="143">
              </el-table-column>
              <el-table-column prop="speed" label="当前风速" width="143">
              </el-table-column>
              <el-table-column prop="currTemp" label="当前温度" width="143">
              </el-table-column>
              <el-table-column prop="targetTemp" label="目标温度" width="143">
              </el-table-column>
              <el-table-column prop="servedTime" label="服务时间" width="143">
              </el-table-column>
              <el-table-column prop="fee" label="服务费用" width="">
              </el-table-column>
            </el-table>
          </div>
        </div>
      </el-tab-pane>

      <!-- 设置参数面板 -->
      <el-tab-pane label="设置参数">
        <div class="content">
          <div class="params-form">
            <el-form label-width="100px" size="small" class="login-form">
              <el-form-item label="默认模式">
                <el-radio-group v-model="params.defaultMode">
                  <el-radio :label="'hot'">hot</el-radio>
                  <el-radio :label="'cold'">cold</el-radio>
                </el-radio-group>
              </el-form-item>

              <el-form-item label="制冷温控区间">
                <el-row>
                  <el-col :span="8" :offset="2">
                    <el-input
                      type="number"
                      v-model="params.coldLow"
                      placeholder="最低温度"
                    ></el-input>
                  </el-col>
                  <el-col :span="1" :offset="1">-</el-col>
                  <el-col :span="8" :offset="1">
                    <el-input
                      type="number"
                      v-model="params.coldHigh"
                      placeholder="最高温度"
                    ></el-input>
                  </el-col>
                </el-row>
              </el-form-item>

              <el-form-item label="制热温控区间">
                <el-row>
                  <el-col :span="8" :offset="2">
                    <el-input
                      type="number"
                      v-model="params.hotLow"
                      placeholder="最低温度"
                    ></el-input>
                  </el-col>
                  <el-col :span="1" :offset="1">-</el-col>
                  <el-col :span="8" :offset="1">
                    <el-input
                      type="number"
                      v-model="params.hotHigh"
                      placeholder="最高温度"
                    ></el-input>
                  </el-col>
                </el-row>
              </el-form-item>

              <el-form-item label="缺省温度">
                <el-row>
                  <el-col :span="8" :offset="8">
                    <el-input
                      type="number"
                      v-model="params.defaultTemp"
                      placeholder="缺省温度"
                    ></el-input>
                  </el-col>
                </el-row>
              </el-form-item>

              <el-form-item label="费率">
                <el-row>
                  <el-col :span="8" :offset="8">
                    <el-input
                      type="number"
                      v-model="params.feeRate"
                      placeholder="费率"
                    ></el-input>
                  </el-col>
                </el-row>
              </el-form-item>

              <el-form-item label="服务对象数">
                <el-row>
                  <el-col :span="8" :offset="8">
                    <el-input
                      type="number"
                      v-model="params.scheduledNum"
                      placeholder="服务对象数"
                    ></el-input>
                  </el-col>
                </el-row>
              </el-form-item>

              <el-form-item>
                <el-button type="primary" @click="setDefaultParams(params)">
                  设置默认参数
                </el-button>
              </el-form-item>
            </el-form>
          </div>
        </div>
      </el-tab-pane>
    </el-tabs>
  </div>
</template>

<script>
import { mapActions, mapState } from "vuex";
export default {
  data: function () {
    return {
      tabPosition: "left",
      params: {
        defaultMode: "cold",
        coldHigh: 25,
        coldLow: 18,
        hotHigh: 30,
        hotLow: 25,
        feeRate: 1,
        defaultTemp: 25,
        scheduledNum: 3,
      },
    };
  },
  computed: {
    ...mapState("administrator", ["roomsState", "stateIsOk"]),
  },
  methods: {
    ...mapActions("administrator", ["checkRoomsState", "setDefaultParams"]),
  },
  mounted: function () {
    let that = this;
    that.checkRoomsState();
    if (this.timer) {
      clearInterval(this.timer);
    } else {
      this.timer = setInterval(() => {
        let that = this;
        that.checkRoomsState();
      }, 1000);
    }
  },
  destroyed: function () {
    clearInterval(this.timer);
  },
};
</script>

<style >
.content {
  margin-top: 50px;
  margin-left: 10%;
  margin-right: 10%;
  /* background-color: pink; */
  background-color: #fff;
}
.params-form {
  border-radius: 30px;
  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
  margin-right: 20%;
  margin-left: 20%;
  margin-bottom: 50px;
  padding-top: 30px;
  padding-left: 40px;
  padding-right: 40px;
  padding-bottom: 25px;
}
</style>