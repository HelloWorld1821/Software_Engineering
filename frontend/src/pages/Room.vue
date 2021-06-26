<!--
 * @Description: 
 * @Author: l
 * @Date: 2021-06-01 15:34:21
 * @LastEditors: l
 * @LastEditTime: 2021-06-26 15:34:16
 * @FilePath: \DistributedControlSystem\frontend\src\pages\Room.vue
-->
<template>
  <div>
    <!-- <h1>用户房间{{ roomId }}</h1> -->
    <!-- 空调控制器 -->
    <div class="ac-control">
      <el-row style="margin-top: 20px">
        <el-col><h2>空调控制器</h2></el-col>
      </el-row>

      <el-row style="margin-top: 20px">
        <el-col :span="8" :offset="0" class="temp">
          <div>目标温度:</div>
        </el-col>
        <el-col :span="8" :offset="2">
          <div>
            <el-input-number
              v-model="targetTemp"
              :min="10"
              :max="40"
              size="small"
            >
            </el-input-number>
          </div>
        </el-col>
      </el-row>

      <el-row style="margin-top: 20px">
        <el-col :span="8" :offset="0" class="temp">
          <div>目标风速:</div>
        </el-col>
        <el-col :offset="0" style="margin-top: 10px">
          <el-radio-group v-model="targetSpeed">
            <el-radio :label="'low'">Low</el-radio>
            <el-radio :label="'mid'">Mid</el-radio>
            <el-radio :label="'high'">High</el-radio>
          </el-radio-group>
        </el-col>
      </el-row>

      <el-row style="margin-top: 20px">
        <el-col :span="8" :offset="0" class="state">
          <div>
            <div>空调状态:</div>
          </div>
        </el-col>
        <el-col :span="4" :offset="5"
          ><div>
            <el-switch
              v-model="acStateBool"
              active-color="#13ce66"
              inactive-color="#ff4949"
            >
            </el-switch></div
        ></el-col>
      </el-row>

      <el-row class="update" style="margin-top: 30px">
        <el-button size="medium" type="primary" @click="updateRoomState(roomId)"
          >手动更新房间状态</el-button
        >
      </el-row>
    </div>

    <div class="user-panel">
      <el-row style="margin-top: 20px">
        <el-col><h2>房间状态</h2></el-col>
      </el-row>
      <el-row style="margin-top: 20px">
        <el-col :span="8" :offset="0" class="temp">
          <div>房间ID:</div>
        </el-col>
        <el-col :span="8" :offset="4">
          <div>
            {{ roomId }}
          </div>
        </el-col>
      </el-row>
      <el-row style="margin-top: 20px">
        <el-col :span="8" :offset="0" class="state">
          <div>
            <div>休眠模式:</div>
          </div>
        </el-col>
        <el-col :span="4" :offset="6"
          ><div>
            <el-switch

              disabled=true
              v-model="sleepMode"
              active-color="#13ce66"
              inactive-color="#ff4949"
            >
            </el-switch></div
        ></el-col>
      </el-row>
      <el-row style="margin-top: 20px">
        <el-col :span="8" :offset="0" class="temp">
          <div>送风状态:</div>
        </el-col>
        <el-col :span="8" :offset="4">
          <div>
            {{ roomState.acState }}
          </div>
        </el-col>
      </el-row>

      <el-row style="margin-top: 20px">
        <el-col :span="8" :offset="0" class="temp">
          <div>当前温度:</div>
        </el-col>
        <el-col :span="8" :offset="4">
          <div>
            {{ roomState.currTemp }}
          </div>
        </el-col>
      </el-row>

      <el-row style="margin-top: 20px">
        <el-col :span="8" :offset="0" class="temp">
          <div>当前风速:</div>
        </el-col>
        <el-col :span="8" :offset="4">
          <div>
            {{ roomState.speed }}
          </div>
        </el-col>
      </el-row>

      <el-row style="margin-top: 20px">
        <el-col :span="8" :offset="0" class="temp">
          <div>当前费用:</div>
        </el-col>
        <el-col :span="8" :offset="4">
          <div>
            {{ roomState.fee }}
          </div>
        </el-col>
      </el-row>
    </div>
  </div>
</template>

<script>
import { mapActions, mapState } from "vuex";
export default {
  data: function () {
    return {
      targetTemp: null,
      targetSpeed: null,
      targetACState: "off",
      acStateBool: false,
      sleepMode: false, //是否开启休眠模式
    };
  },
  created() {
    this.targetTemp = this.roomParams.targetTemp;
    this.targetSpeed = this.roomParams.targetSpeed;
  },
  computed: {
    ...mapState("room", ["roomId", "roomState", "roomParams"]),
  },
  methods: {
    ...mapActions("room", ["updateRoomState", "changeRoomState"]),

    // 这个函数只是为了简化实现
    tryChangeRoomState() {
      // 启动定时器防止1s内多次操作，以最后一次为主
      if (this.launchTimer != null) {
        //若原来计时器存在，则打断该请求
        clearInterval(this.launchTimer);
      }
      this.launchTimer = setTimeout(() => {
        this.changeRoomState({
          roomId: this.roomId,
          targetTemp: this.targetTemp,
          targetSpeed: this.targetSpeed,
          targetACState: this.targetACState,
        });
      }, 1000);
    },
    //停止送风请求，送停风请求
    stopAirSupply() {
      console.log("stopAirSupply..");
      this.changeRoomState({
        roomId: this.roomId,
        targetTemp: this.targetTemp,
        targetSpeed: this.targetSpeed,
        targetACState: "off", //在服务器看来就是关闭空调,发送sleep消息，与off不一样
      });
    },
    //启动送风服务，送送风请求
    startAirSupply() {
      console.log("startAirSupply..");
      this.changeRoomState({
        roomId: this.roomId,
        targetTemp: this.targetTemp,
        targetSpeed: this.targetSpeed,
        targetACState: "on", //在服务器看来就是打开空调
      });
    },
    handlerTempChange(cTemp, tTemp) {
      if (this.acStateBool == false) return;
      if (this.roomParams.mode == "cold") {
        //制冷模式
        console.log('sleep on currTemp:',cTemp,'targetTemp:',tTemp,'mode',this.sleepMode);
        if (cTemp <= tTemp) {
          
          this.sleepMode = true; //打开休眠模式
          this.stopAirSupply();
        } else {
          if (cTemp - tTemp >= 1 && this.sleepMode == true) {
            this.sleepMode = false; //关闭休眠模式
            this.startAirSupply();
          } else {
          }
        }
      } else if (this.roomParams.mode == "hot") {
        //制热模式
        if (cTemp >= tTemp) {
          this.sleepMode = true; //打开休眠模式
          this.stopAirSupply();
        } else {
          if (tTemp - cTemp >= 1 && this.sleepMode == true) {
            this.sleepMode = false;
            this.startAirSupply();
          }
        }
      }
    },
  },
  watch: {
    acStateBool: function (newValue, oldValue) {
      if (newValue == true) this.targetACState = "on";
      if (newValue == false) this.targetACState = "off";
    },
    targetTemp: function (newValue, oldValue) {
      // console.log("targetTemp: " + oldValue + "-->" + newValue);
      this.$store.commit("room/setTargetTemp", newValue);
      // var cTemp = parseInt(this.roomState.currTemp);
      // var tTemp = parseInt(this.targetTemp);
      // handlerTempChange(cTemp,tTemp);
      
      // 目标温度改变，关闭休眠模式
      this.sleepMode = false;
      this.tryChangeRoomState();
    },
    targetSpeed: function (newValue, oldValue) {
      // console.log("targetSpeed: " + oldValue + "-->" + newValue);
      if (this.acStateBool == true) this.tryChangeRoomState();
    },
    targetACState: function (newValue, oldValue) {
      // console.log("targetACState: " + oldValue + "-->" + newValue);
      // 空调状态改变，关闭休眠模式
      this.sleepMode = false;
      this.tryChangeRoomState();
    },
    roomState: function (newValue, oldValue) {
      // console.log("roomState change , currTemp:",newValue.currTemp);
      var cTemp = parseFloat(newValue.currTemp);
      var tTemp = parseFloat(this.targetTemp);
      this.handlerTempChange(cTemp,tTemp);
    },
  },
  mounted: function () {
    let that = this;
    that.updateRoomState({ roomId: that.roomId });
    if (this.timer) {
      clearInterval(this.timer);
    } else {
      this.updateTimer = setInterval(() => {
        let that = this;
        that.updateRoomState({ roomId: that.roomId });
      }, 4000);
    }
  },
  destroyed: function () {
    clearInterval(this.updateTimer);
    clearTimeout(this.launchTimer);

    //销毁时看作关机请求
    this.targetACState = "off";
    this.changeRoomStateHere();
  },
};
</script>

<style>
.user-panel {
  background-color: white;
  margin-top: 100px;
  margin-right: 20%;
  padding: 20px;
  /* display: inline-block; */
  float: right;
  width: 300px;
  height: 400px;
  /* float: left; */
  border-radius: 30px;
  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
}
.ac-control {
  background-color: #fff;
  margin-top: 100px;
  margin-left: 20%;
  padding-top: 30px;
  padding-left: 20px;
  padding-right: 20px;
  padding-bottom: 20px;
  /* display: inline-block; */
  height: 400px;
  width: 300px;
  float: left;
  /* float: left; */
  border-radius: 30px;
  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
}
</style>