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
    <el-tabs :tab-position="tabPosition" style="height: 1000px">
      <el-tab-pane label="获取账单">
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
                    type="primary"
                    @click="getBill({ roomId: inputBillRoomId })"
                  >
                    获取账单Bill
                  </el-button>
                </div>
              </el-col>
            </el-row>
          </div>

          <div class="bill-form">
            <el-form label-width="100px" size="small" class="login-form">
              <el-form-item label="房间ID">
                <el-row>{{ billRoomId }}</el-row>
              </el-form-item>
              <el-form-item label="费用">
                <el-row>{{ bill.fee }}</el-row>
              </el-form-item>
            </el-form>
          </div>
        </div>
      </el-tab-pane>

      <el-tab-pane label="获取详单">
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
                  <el-button
                    type="primary"
                    @click="getRDR({ roomId: inputRDRRoomId })"
                  >
                    获取详单RDR
                  </el-button>
                </div>
              </el-col>
            </el-row>
          </div>

          <div class="rdr-table">
            <el-table :data="RDR" border style="width: 100%">
              <el-table-column  sortable prop="startTime" label="起始时间" width="286">
              </el-table-column>
              <el-table-column  sortable prop="endTime" label="结束时间" width="286">
              </el-table-column>
              <el-table-column  sortable prop="speed" label="风速" width="286">
              </el-table-column>
              <el-table-column  sortable prop="fee" label="费用" width="">
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
  data: function () {
    return {
      tabPosition: "left",
      inputBillRoomId: 1,
      inputRDRRoomId: 2,
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
    ]),
  },
  methods: {
    ...mapActions("receptionist", ["getRDR", "getBill"]),
  },
};
</script>
<style>
.content {
  margin-top: 50px;
  margin-left: 10%;
  margin-right: 10%;
  background-color: #fff;
}
.bill-form{
  border-radius: 30px;
  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
  margin-right: 20%;
  margin-left: 20%;
  margin-top: 50px;
  margin-bottom: 50px;
  padding-top: 50px;
  padding-left: 40px;
  padding-right: 40px;
  padding-bottom: 25px;
}

.rdr-table {
  margin-top: 50px;
}
</style>