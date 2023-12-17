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
                    {{ adminStatus.status }}
                  </div>
                </el-col>
              </el-row>
              <el-row style="margin-top: 20px">
                <el-col :span="8" :offset="0" class="temp">
                  <div>设定温度:</div>
                </el-col>
                <el-col :span="8" :offset="4">
                  <div>
                    {{ adminStatus.target_temperature }}
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
import {mapActions, mapState} from "vuex";
import {Message} from "element-ui"; // 使用Element-UI的Message组件

export default {
  destroyed: function () {
    clearInterval(this.timer);
  },
  data: function () {
    return {
      targetTemp: this.$store.state.room.roomParams.defaultTemp,
      fan_speed: this.$store.state.room.roomParams.defaultSpeed,
      targetACState: "off",
      acStateBool: false,//对于空调开关按钮的监控
      sleepMode: false, //是否开启休眠模式
      isSupplyBool: false
    };
  },

  computed: {
    ...mapState("room", [
      "roomId",
      "roomState",
      "roomParams",
      "showState",
      "room_id",
      "adminStatus"
    ]),
    ...mapState("auth", ["room_id"])
  },
  mounted() {
    console.log("mounted.., room_id:", this.room_id);

    //确保room_id已定义，不是空值
    if (this.room_id) {
      this.showRoomState1({room_id: this.room_id});
    }

    if (this.timer) {
      clearInterval(this.timer);
    }

    this.timer = setInterval(() => {
      //确保在定时器中room_id已定义
      if (this.room_id) {
        this.showRoomState1({room_id: this.room_id});
      }
    }, 1000);
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
      this.showRoomState1({room_id: this.room_id});
      console.log("showRoom..");
    },

    on() {
      this.request_on({//调用api接口，启动空调
        room_id: this.room_id
      });
      this.status = "开机"; //更新状态为开机
      this.showSuccessMessage("空调已开启"); //显示操作成功的消息
    },
    off() {
      this.request_off({//调用api接口，关闭空调
        room_id: this.room_id
      });
      this.status = "关机"; //更新状态为关机
      this.showSuccessMessage("空调已关闭"); //显示操作成功的消息
    },

    showSuccessMessage(message) {
      //使用Element-UI的Message组件显示操作成功的返回信息
      Message.success({
        message: message,
        duration: 2000 //持续显示时间(ms)
      });
    },
    decreaseTemp() {
      if (this.targetTemp > this.$store.state.room.roomParams.tempSectionLow) {
        this.targetTemp -= 1;
        this.request_temp({//调用api接口，调整空调温度
          room_id: this.room_id,
          target_temperature: this.targetTemp
        });
      }
    },
    increaseTemp() {
      if (this.targetTemp < this.$store.state.room.roomParams.tempSectionHigh) {
        this.targetTemp += 1;
        this.request_temp({//调用api接口，调整空调温度
          room_id: this.room_id,
          target_temperature: this.targetTemp
        });
      }
    },

    increaseSpeed() {
      if (this.fan_speed === "low") {//控制空调风速只能在三个值之间变化
        this.fan_speed = "medium";
      } else if (this.fan_speed === "medium") {
        this.fan_speed = "high";
      }
      this.request_speed({//调用api接口，调整空调风速
        room_id: this.room_id,
        fan_speed: this.fan_speed
      });
    },
    decreaseSpeed() {
      if (this.fan_speed === "high") {//控制空调风速只能在三个值之间变化
        this.fan_speed = "medium";
      } else if (this.fan_speed === "medium") {
        this.fan_speed = "low";
      }
      this.request_speed({//调用api接口，调整空调风速
        room_id: this.room_id,
        fan_speed: this.fan_speed
      });
    },
  },
  watch: {
    acStateBool: function (newBool, oldBool) {//监控空调按钮的状态
      if (newBool === true) {
        this.on(); //打开空调
      } else {
        this.off(); //关闭空调
      }
    },
    adminStatus: function (newStatus, oldStatus) {//监控adminStatus.status
      if (
        newStatus.status === "SLEEPING" ||
        newStatus.status === "WAITING" ||
        newStatus.status === "SERVING"
      ) {
        // 当adminStatus.status是"SLEEPING"、"WAITING"或 "SERVING" 时，将开关状态设为打开
        this.acStateBool = true;
      } else {
        // 其他情况下，将开关状态设为关闭
        this.acStateBool = false;
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
  height: 600px;
  width: 1000px;
  border-radius: 50px;
  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
}

.user-panel {
  background-color: rgba(255, 255, 255, 0.8);
  margin-top: 20px;
// margin-left: 15%; padding: 20px; // display: inline-block; // float: right; width: 300px; height: 400px;
// float: left; border-radius: 30px;
  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
}

.ac-control {
  background-color: rgba(255, 255, 255, 0.8);
  margin-top: 20px;
//margin-left: 15%; padding: 20px; //float: right; width: 300px; height: 400px;
  border-radius: 30px;
  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
}

.circle-panel {
  display: flex;
  flex-direction: column;
  align-items: center;
  border: 5px solid dodgerblue; /* 边框颜色 */
  border-radius: 50%; /* 创建圆形边框 */
  padding: 20px;
  width: 200px; /* 设置圆圈两个轴的长度 */
  height: 200px;
  margin: auto;
  margin-top: 5px;
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
