<!--
 * @Description: 
 * @Author: l
 * @Date: 2021-06-01 15:34:21
 * @LastEditors: l
 * @LastEditTime: 2021-06-25 18:09:13
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
              :max="30"
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
          <el-radio-group v-model="radioSpeed">
            <el-radio :label="3">Low</el-radio>
            <el-radio :label="6">Mid</el-radio>
            <el-radio :label="9">High</el-radio>
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

    <!-- <div class="user-panel">
      <template>
        <h2 class="mb-0">User Panel</h2>
      </template>
      <p>Your ID Card Number: {{ roomId }}</p>
      <p>Is Running : {{ roomState.acState }}</p>
      <p>The Speed: {{ roomState.speed }}</p>
      <p>Current Temperature: {{ roomState.currTemp }}</p>
      <p>Target Temperature: {{ roomState.targetTemp }}</p>
      <p>Your Cost : {{ roomState.fee }}</p>
    </div> -->
    <!-- <div class="user-panel">
      <el-container>
        <el-header>User Panel</el-header>

        <el-container class="display">
          <el-aside>Your ID Card Number:</el-aside>
          <el-main>{{ roomId }}</el-main>
        </el-container>

        <el-container class="display">
          <el-aside>Is Running :</el-aside>
          <el-main>{{ roomState.acState }}</el-main>
        </el-container>

        <el-container class="display">
          <el-aside>The Speed:</el-aside>
          <el-main>{{ roomState.speed }}</el-main>
        </el-container>

        <el-container class="display">
          <el-aside>Current Temperature:</el-aside>
          <el-main>{{ roomState.currTemp }}</el-main>
        </el-container>

        <el-container class="display">
          <el-aside>Target Temperature:</el-aside>
          <el-main>{{ roomState.targetTemp }}</el-main>
        </el-container>

        <el-container class="display">
          <el-aside>Your Cost:</el-aside>
          <el-main>{{ roomState.fee }}</el-main>
        </el-container>
      </el-container>
    </div> -->
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
            {{roomId}}
          </div>
        </el-col>
      </el-row>
      <el-row style="margin-top: 20px">
        <el-col :span="8" :offset="0" class="temp">
          <div>空调状态:</div>
        </el-col>
        <el-col :span="8" :offset="4">
          <div>
            {{roomState.acState}}
          </div>
        </el-col>
      </el-row>

      <el-row style="margin-top: 20px">
        <el-col :span="8" :offset="0" class="temp">
          <div>当前温度:</div>
        </el-col>
       <el-col :span="8" :offset="4">
          <div>
            {{roomState.currTemp}}
          </div>
       </el-col>
      </el-row>

       <el-row style="margin-top: 20px">
        <el-col :span="8" :offset="0" class="temp">
          <div>当前风速:</div>
        </el-col>
       <el-col :span="8" :offset="4">
          <div>
            {{roomState.speed}}
          </div>
       </el-col>
      </el-row>

      <el-row style="margin-top: 20px">
        <el-col :span="8" :offset="0" class="temp">
          <div>当前费用:</div>
        </el-col>
        <el-col :span="8" :offset="4">
          <div>
            {{roomState.fee}}
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
      targetTemp: 20,
      targetSpeed: "low",
      targetACState: "off",
      acStateBool:false,
      radioSpeed: 6,
    };
  },
  computed: {
    ...mapState("room", ["roomId", "roomState"]),
  },
  methods: {
    ...mapActions("room", ["updateRoomState", "changeRoomState"]),
    // addCurrTemp() {
    //   this.targetTemp = this.targetTemp + 1;
    // },
    // subCurrTemp() {
    //   if (this.targetTemp > 0) this.targetTemp = this.targetTemp - 1;
    // },
    // 这个函数只是为了简化参数
    changeRoomStateHere() {
      // 启动定时器防止1s内多次操作，以最后一次为主
      
      this.changeRoomState({
        targetTemp: this.targetTemp,
        targetSpeed: this.targetSpeed,
        targetACState: this.targetACState,
      });
    },
  },
  watch: {
    radioSpeed: function (newValue, oldValue) {
      if (newValue == 3) this.targetSpeed = "low";
      if (newValue == 6) this.targetSpeed = "mid";
      if (newValue == 9) this.targetSpeed = "high";
    },
    acStateBool:function(newValue,oldValue){
      if(newValue == true) this.targetACState = "on";
      if(newValue == false) this.targetACState = "off";
    },
    targetTemp: function (newValue, oldValue) {
      console.log("targetTemp: " + oldValue + "-->" + newValue);
      this.$store.commit("room/setTargetTemp", newValue);
      this.changeRoomStateHere();
    },
    targetSpeed: function (newValue, oldValue) {
      console.log("targetSpeed: " + oldValue + "-->" + newValue);
      this.changeRoomStateHere();
    },
    targetACState: function (newVaule, oldValue) {
      console.log("targetACState: " + oldValue + "-->" + newVaule);
      this.changeRoomStateHere();
    },
  },
  mounted: function () {
    let that = this;
    that.updateRoomState(that.roomId);
    if (this.timer) {
      clearInterval(this.timer);
    } else {
      this.timer = setInterval(() => {
        let that = this;
        // that.checkRoomsState();
        // that.updateRoomState(that.roomId);
      }, 1000);
    }
  },
  destroyed: function () {
    clearInterval(this.timer);
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