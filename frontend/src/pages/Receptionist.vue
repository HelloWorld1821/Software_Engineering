<!--
 * @Description: 
 * @Author: l
 * @Date: 2021-06-01 15:38:49
 * @LastEditors: l
 * @LastEditTime: 2021-06-04 15:23:34
 * @FilePath: \DistributedControlSystem\frontend\src\pages\Receptionist.vue
-->
<template>
  <div>
      <h2>Receptionists</h2>
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
      </div>
  </div>
</template>

<script>
import { computed } from '@vue/composition-api'
import { mapActions, mapState } from 'vuex'
export default {
  data:function(){
    return {
      inputBillRoomId:1,
      inputRDRRoomId:2,
    }
  },
  computed:{
    ...mapState('receptionist',[
      'RDRRoomId',
      'billRoomId',
      'RDR',
      'bill',
      'RDRIsOk',
      'billIsOk',
    ])
  },
  methods:{
    ...mapActions('receptionist',[
      'getRDR',
      'getBill',
    ])
  }
}
</script>
<style>
.bill-div ,.RDR-div{
  margin-top: 10px;
  margin-left: 30%;
  margin-right: 30%;
  background-color: #fff;
}
</style>