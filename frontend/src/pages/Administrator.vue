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

    <el-tabs :type="border - card" style="height:500px">
      <!-- 管理员监视面板 -->
      <el-tab-pane>
        <template slot="label">
          <div class="label" style="color: rgb(226, 183, 43);">
            <h2>监视房间</h2>
          </div>
        </template>
        <div class="content">
          <h2>房间监视情况：</h2>
          <div class="rooms-table">
            <el-table :data="roomsState" border style="width: 100%">
              <el-table-column prop="room_id" label="房间ID" width="143">
              </el-table-column>

              <el-table-column prop="status" label="空调模式" width="143">
              </el-table-column>
              <el-table-column prop="fan_speed" label="当前风速" width="143">
              </el-table-column>
              <el-table-column
                prop="current_temperature"
                label="当前温度"
                width="143"
              >
              </el-table-column>
              <el-table-column
                prop="initial_temperature"
                label="初始温度"
                width="143"
              >
              </el-table-column>
              <el-table-column
                prop="target_temperature"
                label="目标温度"
                width="143"
              >
              </el-table-column>
              <el-table-column prop="server_time" label="服务时间" width="143">
              </el-table-column>
              <el-table-column prop="total_cost" label="服务费用" width="">
              </el-table-column>
              <el-table-column
                prop="identity_card"
                label="身份证号"
                width="143"
              >
              </el-table-column>
            </el-table>
          </div>
        </div>
      </el-tab-pane>

      <!-- 设置参数面板 -->
      <el-tab-pane>
        <template slot="label">
          <div class="label" style="color: rgb(226, 183, 43);">
            <h2>设置参数</h2>
          </div>
        </template>
        <div class="content">
          <h2>设置参数：</h2>
          <div class="params-form">
            <el-form label-width="100px" size="small" class="login-form">
              <el-form-item label="房间ID">
                <el-row>
                  <el-col :span="8" :offset="8">
                    <el-input
                      type="number"
                      v-model="params.roomId"
                      placeholder="请输入房间ID"
                    ></el-input>
                  </el-col>
                </el-row>
              </el-form-item>

              <el-form-item label="目标温度">
                <el-row>
                  <el-col :span="8" :offset="8">
                    <el-input
                      type="number"
                      v-model="params.target_Temp"
                      placeholder="目标温度"
                    ></el-input>
                  </el-col>
                </el-row>
              </el-form-item>

              <el-form-item label="风速">
                <el-row>
                  <el-col :span="8" :offset="8">
                    <el-select
                      v-model="params.fanSpeed"
                      placeholder="请选择风速"
                    >
                      <el-option label="高风速" value="high"></el-option>
                      <el-option label="中风速" value="medium"></el-option>
                      <el-option label="低风速" value="low"></el-option>
                    </el-select>
                  </el-col>
                </el-row>
              </el-form-item>

              <el-form-item label="空调状态">
                <el-row>
                  <el-col :span="8" :offset="8">
                    <el-select
                      v-model="params.Status"
                      placeholder="请选择空调状态"
                    >
                      <el-option label="服务中" value="SERVING"></el-option>
                      <el-option label="等待中" value="WAITING"></el-option>
                      <el-option label="已关闭" value="SHUTDOWN"></el-option>
                      <el-option label="休眠中" value="SLEEPING"></el-option>
                    </el-select>
                  </el-col>
                </el-row>
              </el-form-item>

              <el-form-item>
                <el-button type="primary" @click="callSetDefaultParams(params)">
                  设置参数
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
  data: function() {
    return {
      tabPosition: "left",
      params: {
        roomId: 1,
        target_Temp: 25,
        fanSpeed: "high",
        Status: "SERVING"
      }
    };
  },
  computed: {
    ...mapState("administrator", ["roomsState", "stateIsOk"])
  },
  methods: {
    ...mapActions("administrator", ["checkRoomsState", "setDefaultParams"]),
    showSuccessMessage() {
      this.$message.success("操作成功");

      // 在这里可以执行其他操作，如重新加载数据或跳转页面等

      // 以下是示例操作，你可以根据你的需求来处理
      setTimeout(() => {
        // 模拟成功后的操作
        console.log("成功后的操作");
      }, 1000);
    },

    // 在调用 setDefaultParams 后立即调用 showSuccessMessage
    callSetDefaultParams(params) {
      this.setDefaultParams(params);
      this.showSuccessMessage();
    }
  },
  mounted: function() {
    let that = this;
    that.checkRoomsState();
    if (this.timer) {
      clearInterval(this.timer);
    } else {
      this.timer = setInterval(() => {
        let that = this;
        that.checkRoomsState();
      }, 3000);
    }
  },
  destroyed: function() {
    clearInterval(this.timer);
  }
};
</script>

<style scoped>
.content {
  margin-top: 50px;
  margin-left: 5%;
  margin-right: 5%;
  /* background-color: pink; */
  backdrop-filter: blur(10px);
  background: linear-gradient(rgba(255, 255, 255, 0.1), rgba(0, 0, 0, 0.5));
  box-shadow: 0 20px 40px 3px rgba(0, 0, 0, 0.253);
  border-radius: 30px;
  height: 500px;
}
.rooms-table {
  padding-top: 60px;
}
.login-form {
  width: 100%;
  padding-top: 60px;
}
.params-form {
  border-radius: 30px;
  box-shadow: 0 2px 12px 0 rgba(55, 55, 55, 0.245);
  margin-right: 20%;
  margin-left: 20%;

  padding-left: 40px;
  padding-right: 40px;
  padding-bottom: 25px;
  background-color: rgba(221, 221, 221, 0.826);
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
