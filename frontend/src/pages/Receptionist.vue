<template>
  <div>
    <el-tabs :type="border - card" style="height: 500px">
      <el-tab-pane>
        <template slot="label">
          <div class="label" style="color: rgb(226, 183, 43)">
            <h2>获取账单</h2>
          </div>
        </template>
        <div class="content">
          <div class="search-header">
            <el-row align="middle" type="flex">
              <el-col :span="6" :offset="2">
                <div class="grid-content">
                  <h4>请输入要查询的房间ID:</h4>
                </div>
              </el-col>
              <el-col :span="4" :offset="0" align="middle" type="flex">
                <div class="grid-content input-roomid">
                  <el-input placeholder="room id" v-model="room_id" clearable>
                  </el-input>
                </div>
              </el-col>
              <el-col :span="2" :offset="1" align="middle" type="flex">
                <div class="grid-content bg-purple-light">
                  <el-button round @click="getBill({ room_id: room_id })">
                    获取账单
                  </el-button>
                </div>
              </el-col>

              <el-col :span="9" :offset="1" align="middle" type="flex">
                <div class="grid-content bg-purple-light">
                  <el-button
                    style="background-color: rgba(234, 150, 150, 0.811);"
                    round
                    @click="DeleteRoom({ room_id: room_id })"
                  >
                    退房
                  </el-button>
                </div>
              </el-col>
            </el-row>
          </div>

          <div class="bill-form">
            <el-form label-width="100px" size="small" class="login-form">
              <el-form-item>
                <template slot="label">
                  <div class="label" style="color: rgb(0, 0, 0)">
                    <h3>房间ID</h3>
                  </div>
                </template>
                <el-row class="text">{{ room_id }}</el-row>
              </el-form-item>
              <el-form-item>
                <template slot="label">
                  <div class="label" style="color: rgb(0, 0, 0)">
                    <h3>费用</h3>
                  </div>
                </template>
                <el-row class="text">{{ totalCost }}</el-row>
              </el-form-item>
            </el-form>
          </div>
        </div>
      </el-tab-pane>

      <el-tab-pane>
        <template slot="label">
          <div class="label" style="color: rgb(226, 183, 43)">
            <h2>获取详单</h2>
          </div>
        </template>
        <div class="content">
          <div class="search-header">
            <el-row align="middle" type="flex">
              <el-col :span="6" :offset="2">
                <div class="grid-content">
                  <h4>请输入要查询的房间ID:</h4>
                </div>
              </el-col>
              <el-col :span="4" :offset="0" align="middle" type="flex">
                <div class="grid-content input-roomid">
                  <el-input
                    placeholder="room id"
                    v-model="inputRDRRoomId"
                    clearable
                  >
                  </el-input>
                </div>
              </el-col>
              <el-col :span="2" :offset="1" align="middle" type="flex">
                <div class="grid-content bg-purple-light">
                  <el-button round @click="handleGetRDR">
                    获取详单
                  </el-button>
                </div>
              </el-col>
            </el-row>
          </div>

          <div class="rdr-table">
            <el-table :data="RDR" border style="width: 100%">
              <el-table-column
                sortable
                prop="start_time"
                label="起始时间"
                width="286"
              >
              </el-table-column>
              <el-table-column
                sortable
                prop="end_time"
                label="结束时间"
                width="286"
              >
              </el-table-column>
              <el-table-column
                sortable
                prop="fan_speed"
                label="风速"
                width="286"
              >
              </el-table-column>
              <el-table-column
                sortable
                prop="current_cost"
                label="费用"
                width=""
              >
              </el-table-column>
            </el-table>
          </div>
        </div>
      </el-tab-pane>

      <el-tab-pane>
        <template slot="label">
          <div class="label" style="color: rgb(226, 183, 43)">
            <h2>入住登记</h2>
          </div>
        </template>
        <div class="content">
          <el-row align="middle" type="flex" class="content2">
            <el-row :gutter="20" align="middle">
              <!-- 房间ID -->
              <el-col :span="24">
                <div class="grid-content">
                  <h4>请输入登记房间:</h4>
                  <el-input placeholder="room id" v-model="room_id" clearable>
                  </el-input>
                </div>
              </el-col>

              <!-- 身份证号 -->
              <el-col :span="24">
                <div class="grid-content">
                  <h4>请输入身份证号:</h4>
                  <el-input
                    placeholder="identity card"
                    v-model="identity_card"
                    clearable
                  >
                  </el-input>
                </div>
              </el-col>

              <!-- 初始温度 -->
              <el-col :span="24">
                <div class="grid-content">
                  <h4>请输入初始温度:</h4>
                  <el-input
                    placeholder="initial temperature"
                    v-model="initial_temperature"
                    clearable
                  >
                  </el-input>
                </div>
              </el-col>

              <!-- 提交按钮 -->

              <el-col
                :span="24"
                :offset="1"
                align="middle"
                type="flex"
                style="margin-top: 30px;margin-left: 30%;"
              >
                <div class="grid-content bg-purple-light">
                  <el-button
                    round
                    @click="
                      CreateRoom({
                        room_id,
                        identity_card,
                        initial_temperature
                      })
                    "
                  >
                    创建房间
                  </el-button>
                </div>
              </el-col>
            </el-row>
          </el-row>
        </div>
      </el-tab-pane>
    </el-tabs>
  </div>
</template>

<script>
import XLSX from "xlsx";
import { computed } from "@vue/composition-api";
import { mapActions, mapState } from "vuex";
export default {
  data: function() {
    return {
      tabPosition: "left",
      room_id: "1",
      inputRDRRoomId: 2,
      identity_card: "1", //修改
      initial_temperature: "1", //修改
      imgSrc: require("../assets/images/room.jpg")
    };
  },
  computed: {
    ...mapState("receptionist", [
      "RDRRoomId",
      "billRoomId",
      "RDR",
      "bill",
      "RDRIsOk",
      "billIsOk",
      "totalCost"
    ])
  },
  methods: {
    ...mapActions("receptionist", [
      "getRDR",
      "getBill",
      "CreateRoom",
      "DeleteRoom"
    ]), //修改
    async handleGetRDR() {
      // 调用Vuex中的getRDR方法
      await this.getRDR({ roomId: this.inputRDRRoomId });

      // 生成并下载Excel文件
      this.generateAndDownloadExcel();
    },

    generateAndDownloadExcel() {
      const ws = XLSX.utils.json_to_sheet(this.RDR);
      const wb = XLSX.utils.book_new();
      XLSX.utils.book_append_sheet(wb, ws, "RDRData");
      const wbout = XLSX.write(wb, { bookType: "xlsx", type: "array" });

      const blob = new Blob([wbout], { type: "application/octet-stream" });
      const fileName = "详单.xlsx";

      if (window.navigator.msSaveOrOpenBlob) {
        // For IE and Edge
        window.navigator.msSaveBlob(blob, fileName);
      } else {
        // For other browsers
        const url = window.URL.createObjectURL(blob);
        const a = document.createElement("a");
        document.body.appendChild(a);
        a.href = url;
        a.download = fileName;
        a.click();
        window.URL.revokeObjectURL(url);
        document.body.removeChild(a);
      }
    }
  }
};
</script>
<style scoped>
.text {
  font-size: 20px;
  color: rgb(0, 4, 27);
  font-weight: bold;
}
.content {
  margin-top: 50px;
  margin-left: 5%;
  margin-right: 5%;

  height: 500px;

  border-radius: 30px;
  backdrop-filter: blur(10px);
  background: linear-gradient(rgba(255, 255, 255, 0.1), rgba(0, 0, 0, 0.5));
  box-shadow: 0 20px 40px 1px rgba(0, 0, 0, 0.12);
}
.search-header {
  backdrop-filter: blur(10px);
  background: linear-gradient(rgba(255, 255, 255, 0.1), rgba(0, 0, 0, 0.25));
  border-radius: 30px;
}
.bill-form {
  border-radius: 30px;
  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.3);
  margin-right: 5%;
  margin-left: 5%;
  margin-top: 50px;
  margin-bottom: 50px;
  padding-top: 50px;
  padding-left: 40px;
  padding-right: 40px;
  padding-bottom: 25px;
  backdrop-filter: blur(10px);
  background: linear-gradient(rgba(255, 255, 255, 0.1), rgba(0, 0, 0, 0.25));
}

.rdr-table {
  margin-top: 50px;
}
.background {
  width: 100%;
  height: 100%; /**宽高100%是为了图片铺满屏幕 */
  z-index: -1;
  position: absolute;
}
</style>
<style>
.el-tabs__item {
  margin-top: -3px;
  margin-left: 10px;
  margin-right: 10px;
  margin-bottom: 15px;
}
.el-tabs__nav-scroll {
  backdrop-filter: blur(10px);
  background: linear-gradient(rgba(255, 255, 255, 0.1), rgba(0, 0, 0, 0.3));
  box-shadow: 0 20px 40px 3px rgba(0, 0, 0, 0.253);
}
/* //修改 */
.content2 {
  /* 使用flex布局 */
  display: flex;
  /* 水平居中 */
  justify-content: center;
  /* 垂直居中 */
  align-items: center;
  /* 上边距 */
  margin-top: 50px;
  /* 左边距，如果您想要居中，可以设置为自动 */
  margin-left: auto;
  /* 右边距，同样设置为自动以实现水平居中 */
  margin-right: auto;
  /* 高度 */
  height: 500px;
  /* 宽度 */
  width: 600px;
}
</style>
