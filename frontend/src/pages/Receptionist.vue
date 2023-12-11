<!--
 * @Description:
 * @Author: l
 * @Date: 2021-06-01 15:38:49
 * @LastEditors: l
 * @LastEditTime: 2021-06-27 00:59:37
 * @FilePath: \DistributedControlSystem\frontend\src\pages\Receptionist.vue
-->
<template>
  <div>
    <!-- <h2>Receptionists</h2>
      <div class='bill-div'>
        Bill RoomId:
        <input type='text' v-model="inputBillRoomId">
        <input type='button' value='getBill' @click="getBill({roomId:inputBillRoomId})">
        <div class='bill' v-if='billIsOk'>
          Bill:
          <p>roomId:{{billRoomId}}</p>
          <p>fee:{{bill.fee}}</p>
        </div>
      </div>
      <div class='RDR-div'>
        RDR RoomId:
        <input type='text' v-model="inputRDRRoomId">
        <input type='button' value='getRDR' @click="getRDR({roomId:inputRDRRoomId})">
        <div class='RDR' v-if='RDRIsOk'>
          RDR:
          <p>roomId:{{RDRRoomId}}</p>
          <p>startTime:{{RDR.startTime}}</p>
          <p>endTime:{{RDR.endTime}}</p>
          <p>speed:{{RDR.speed}}</p>
          <p>fee:{{RDR.fee}}</p>
        </div>
      </div> -->
    <el-tabs :type="border - card" style="height:500px">
      <el-tab-pane>
        <template slot="label">
          <div class="label" style="color: rgb(226, 183, 43);">
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
                  <el-input
                    placeholder="room id"
                    v-model="inputBillRoomId"
                    clearable
                  >
                  </el-input>
                </div>
              </el-col>
              <el-col :span="2" :offset="1" align="middle" type="flex">
                <div class="grid-content bg-purple-light">
                  <el-button
                    round
                    @click="getBill({ roomId: inputBillRoomId })"
                  >
                    获取账单
                  </el-button>
                </div>
              </el-col>
            </el-row>
          </div>

          <div class="bill-form">
            <el-form label-width="100px" size="small" class="login-form">
              <el-form-item>
                <template slot="label">
                  <div class="label" style="color: rgb(0, 0, 0);">
                    <h3>房间ID</h3>
                  </div>
                </template>
                <el-row>{{ billRoomId }}</el-row>
              </el-form-item>
              <el-form-item>
                <template slot="label">
                  <div class="label" style="color: rgb(0, 0, 0);">
                    <h3>费用</h3>
                  </div>
                </template>
                <el-row>{{ bill.fee }}</el-row>
              </el-form-item>
            </el-form>
          </div>
        </div>
      </el-tab-pane>

      <el-tab-pane>
        <template slot="label">
          <div class="label" style="color: rgb(226, 183, 43);">
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
                  <el-button round @click="getRDR({ roomId: inputRDRRoomId })">
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
                prop="startTime"
                label="起始时间"
                width="286"
              >
              </el-table-column>
              <el-table-column
                sortable
                prop="endTime"
                label="结束时间"
                width="286"
              >
              </el-table-column>
              <el-table-column sortable prop="speed" label="风速" width="286">
              </el-table-column>
              <el-table-column sortable prop="fee" label="费用" width="">
              </el-table-column>
            </el-table>
          </div>
        </div>
      </el-tab-pane>
    </el-tabs>
  </div>
</template>

<script>
import { computed } from "@vue/composition-api";
import { mapActions, mapState } from "vuex";
export default {
  data: function() {
    return {
      tabPosition: "left",
      inputBillRoomId: 1,
      inputRDRRoomId: 2,
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
      "billIsOk"
    ])
  },
  methods: {
    ...mapActions("receptionist", ["getRDR", "getBill"])
  }
};
</script>
<style scoped>
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
</style>
