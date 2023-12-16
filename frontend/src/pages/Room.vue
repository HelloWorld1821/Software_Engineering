<template>
  <div>
    <el-row>
      <div class="control_panel">
        <el-row>
          <h2>控制面板</h2>
        </el-row>
        <el-row
          style="display: flex;
  justify-content: space-between; margin-left: 55px"
        >
          <el-col :span="10">
            <div class="user-panel">
              <el-row>
                <el-col><h2>房间状态</h2></el-col>
              </el-row>
              <el-row style="margin-top: 20px">
                <el-col :span="8" :offset="0" class="temp">
                  <div>房间号ID:</div>
                </el-col>
                <el-col :span="8" :offset="4">
                  <div>
                    {{ room_id }}
                  </div>
                </el-col>
              </el-row>
              <el-row style="margin-top: 20px">
                <el-col :span="8" :offset="0" class="temp">
                  <div>当前温度:</div>
                </el-col>
                <el-col :span="8" :offset="4">
                  <div>
                    {{ showState.current_temperature }}
                  </div>
                </el-col>
              </el-row>

              <el-row style="margin-top: 20px">
                <el-col :span="8" :offset="0" class="temp">
                  <div>当前风速:</div>
                </el-col>
                <el-col :span="8" :offset="4">
                  <div>
                    {{ showState.fan_speed }}
                  </div>
                </el-col>
              </el-row>
              <el-row style="margin-top: 20px">
                <el-col :span="8" :offset="0" class="temp">
                  <div>开机状态:</div>
                </el-col>
                <el-col :span="8" :offset="4">
                  <div>
                    {{ status }}
                  </div>
                </el-col>
              </el-row>
              <el-row style="margin-top: 20px">
                <el-col :span="8" :offset="0" class="temp">
                  <div>设定温度:</div>
                </el-col>
                <el-col :span="8" :offset="4">
                  <div>
                    {{ targetTemp }}
                  </div>
                </el-col>
              </el-row>
              <el-row style="margin-top: 20px">
                <el-col :span="8" :offset="0" class="temp">
                  <div>当前费用:</div>
                </el-col>
                <el-col :span="8" :offset="4">
                  <div>
                    {{ showState.total_cost }}
                  </div>
                </el-col>
              </el-row>
            </div>
          </el-col>
          <el-col :span="10">
            <div class="ac-control">
              <el-row>
                <el-col><h2>空调控制器</h2></el-col>
              </el-row>
              <div class="circle-panel">
                <el-row>
                  <el-col :offset="0">
                    <el-button @click="increaseTemp">+</el-button>
                  </el-col>
                  <el-col :offset="0" class="temp">
                    <div>温度+</div>
                  </el-col>
                </el-row>

                <el-row
                  style="margin-top: 20px;margin-bottom: 20px"
                  class="button-row"
                >
                  <el-col :span="6" :offset="0">
                    <el-button @click="decreaseSpeed">-</el-button>
                  </el-col>
                  <el-col :span="6" :offset="0" class="rotate-text">
                    <div>风速-</div>
                  </el-col>
                  <el-col
                    :span="6"
                    style="margin-top: 10px; margin-left: 5px; margin-right: 5px"
                  >
                    <el-switch
                      v-model="acStateBool"
                      active-color="#13ce66"
                      inactive-color="#ff4949"
                    ></el-switch>
                  </el-col>
                  <el-col :span="6" :offset="0" class="rotate-text">
                    <div>风速+</div>
                  </el-col>
                  <el-col :span="6" :offset="0">
                    <el-button @click="increaseSpeed">+</el-button>
                  </el-col>
                </el-row>

                <el-row>
                  <el-col :offset="0" class="temp">
                    <div>温度-</div>
                  </el-col>
                  <el-col :offset="0">
                    <el-button @click="decreaseTemp">-</el-button>
                  </el-col>
                </el-row>
              </div>
              <el-row class="update" style="margin-top: 30px">
                <el-button
                  size="medium"
                  type="primary"
                  @click="showRoom(room_id)"
                  >手动更新房间状态
                </el-button>
              </el-row>
            </div>
          </el-col>
        </el-row>
        <el-row style="text-align: right">
          <h2>费率：1￥/℃</h2>
        </el-row>
      </div>
    </el-row>
  </div>
</template>

<script>
import { mapActions, mapState } from "vuex";

export default {
  destroyed: function() {
    clearInterval(this.timer);
  },
  data: function() {
    return {
      targetTemp: this.$store.state.room.roomParams.defaultTemp,
      fan_speed: this.$store.state.room.roomParams.defaultSpeed,
      targetACState: "off",
      acStateBool: false,
      sleepMode: false, //是否开启休眠模式
      isSupplyBool: false,
      status: "关机" // 默认为'关机'
    };
  },

  computed: {
    ...mapState("room", [
      "roomId",
      "roomState",
      "roomParams",
      "showState",
      "room_id"
    ]),
    ...mapState("auth", ["room_id"])

    // isSupplyBool:()=>{
    //     return this.$store.state.room.roomState.acState;
    // },
  },
  mounted() {
    console.log("mounted.., room_id:", this.room_id);

    // 确保 room_id 已定义
    if (this.room_id) {
      this.showRoomState1({ room_id: this.room_id });
    }

    if (this.timer) {
      clearInterval(this.timer);
    }

    this.timer = setInterval(() => {
      // 同样确保在定时器中 room_id 已定义
      if (this.room_id) {
        this.showRoomState1({ room_id: this.room_id });
      }
    }, 5000);
  },
  methods: {
    ...mapActions("room", [
      "request_on",
      "request_off",
      "request_temp",
      "request_speed",
      "showRoomState",
      "showRoomState1"
    ]),
    showRoom(room_id) {
      this.showRoomState1({ room_id: this.room_id });
      console.log("showRoom..");
    },
    on() {
      this.request_on({
        room_id: this.room_id
      });
      this.status = "开机"; // 更新状态为'开机'
    },
    off() {
      this.request_off({
        room_id: this.room_id
      });
      this.status = "关机"; // 更新状态为'关机'
    },
    decreaseTemp() {
      if (this.targetTemp > this.$store.state.room.roomParams.tempSectionLow) {
        this.targetTemp -= 1;
        // this.tryChangeRoomState(); // 执行相应的操作
        this.request_temp({
          room_id: this.room_id,
          target_temperature: this.targetTemp
        });
      }
    },
    increaseTemp() {
      if (this.targetTemp < this.$store.state.room.roomParams.tempSectionHigh) {
        this.targetTemp += 1;
        // this.tryChangeRoomState(); // 执行相应的操作
        this.request_temp({
          room_id: this.room_id,
          target_temperature: this.targetTemp
        });
      }
    },

    increaseSpeed() {
      if (this.fan_speed === "low") {
        this.fan_speed = "medium";
      } else if (this.fan_speed === "medium") {
        this.fan_speed = "high";
      } // You can add more conditions if needed
      // Call the backend or perform any other actions if required
      // this.tryChangeRoomState();
      this.request_speed({
        room_id: this.room_id,
        fan_speed: this.fan_speed
      });
    },
    decreaseSpeed() {
      if (this.fan_speed === "high") {
        this.fan_speed = "medium";
      } else if (this.fan_speed === "medium") {
        this.fan_speed = "low";
      } // You can add more conditions if needed
      // Call the backend or perform any other actions if required
      // this.tryChangeRoomState();
      this.request_speed({
        room_id: this.room_id,
        fan_speed: this.fan_speed
      });
    },
    // 这个函数只是为了简化实现
    tryChangeRoomState() {
      // 启动定时器防止1s内多次操作，以最后一次为主
      if (this.launchTimer != null) {
        //若原来计时器存在，则打断该请求
        clearInterval(this.launchTimer);
      }
      console.log("tryChangeRoomState..");
      this.launchTimer = setTimeout(() => {
        this.changeRoomState({
          room_id: this.room_id,
          targetTemp: this.targetTemp,
          fan_speed: this.fan_speed,
          targetACState: this.targetACState
        });
      }, 100);
    },
    //停止送风请求，送停风请求
    stopAirSupply() {
      console.log("stopAirSupply..");
      this.changeRoomState({
        roomId: this.roomId,
        targetTemp: this.targetTemp,
        fan_speed: this.fan_speed,
        targetACState: "off" //在服务器看来就是关闭空调,发送sleep消息，与off不一样
      });
    },
    //启动送风服务，送送风请求
    startAirSupply() {
      console.log("startAirSupply..");
      this.changeRoomState({
        roomId: this.roomId,
        targetTemp: this.targetTemp,
        fan_speed: this.fan_speed,
        targetACState: "on" //在服务器看来就是打开空调
      });
    }
  },
  watch: {
    acStateBool: function(newValue, oldValue) {
      if (newValue == true) {
        this.targetACState = "on";
        this.on();
      }
      if (newValue == false) {
        this.targetACState = "off";
        this.off();
      }
    }
  }
};
</script>

<style>
.control_panel {
  background-color: rgba(255, 255, 255, 0.8);
  margin: auto; /* 水平居中 */
  margin-top: 20px;
  padding-top: 10px;
  padding-left: 10px;
  padding-right: 10px;
  padding-bottom: 10px;
  /* display: inline-block; */
  height: 600px;
  width: 1000px;
  /* float: left; */
  /* float: left; */
  border-radius: 50px;
  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
  /* z-index:1;
  position: absolute; */
}

.user-panel {
  background-color: rgba(255, 255, 255, 0.8);
  margin-top: 20px;
  // margin-left: 15%; padding: 20px;
  // display: inline-block;
  // float: right; width: 300px;
  height: 400px;
  // float: left;
  border-radius: 30px;
  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
  /* z-index:1;
    position: absolute; */
}

.ac-control {
  background-color: rgba(255, 255, 255, 0.8);
  margin-top: 20px;
  //margin-left: 15%; padding: 20px;
  /* display: inline-block; */
  //float: right; width: 300px;
  height: 400px;
  /* float: left; */
  border-radius: 30px;
  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
  /* z-index:1;
    position: absolute; */
}

.circle-panel {
  display: flex;
  flex-direction: column;
  align-items: center;
  border: 5px solid dodgerblue; /* Border color */
  border-radius: 50%; /* Creates a circular border */
  padding: 20px; /* Adjust padding as needed */
  width: 200px; /* Set a fixed width for the circular control */
  height: 200px; /* Set a fixed height for the circular control */
  margin: auto; /* Center the circle horizontally */
  margin-top: 5px; /* Adjust margin-top as needed */
}

.rotate-text {
  margin-left: -30px;
  writing-mode: vertical-rl;
  transform: rotate(0deg);
  white-space: nowrap;
  text-align: left;
}

.button-row {
  display: flex;
  justify-content: space-around;
  width: 100%;
}
</style>
