<!--
 * @Description: 
 * @Author: l
 * @Date: 2021-06-01 15:34:21
 * @LastEditors: l
 * @LastEditTime: 2021-06-05 10:52:20
 * @FilePath: \DistributedControlSystem\frontend\src\pages\Room.vue
-->
<template>
  <div>
    <h1>This is Room</h1>
    <div class='ac-control'>
      
      
      <input type="button" @click="subCurrTemp" value="sub">
      {{roomState.targetTemp}}
      <input type="button" @click='addCurrTemp' value="add">

    </div>
    <div class='user-panel'>
      <template>
        <h2 class="mb-0">User Panel</h2>
      </template>
      <p>Your ID Card Number: {{ roomId }}</p>
      <p>Is Running : {{ roomState.acState }}</p>
      <p>The Speed: {{ roomState.speed }}</p>
      <p>Current Temperature: {{ roomState.currTemp }}</p>
      <p>Target Temperature: {{ roomState.targetTemp }}</p>
      <p>Your Cost : {{ roomState.fee }}</p>
    </div>
  </div>
</template>

<script>
import { mapActions, mapState } from "vuex";
export default {
  data: function () {
    return {};
  },
  computed: {
    ...mapState("room", ["roomId", "roomState"]),
    // targetTemp:{
    //   get(){
    //     return this.$store.room.state.roomState.targetTemp;
    //     return 1;
    //   },
    //   set(value){
    //     this.$store.commit('room/setCurrTemp',value);
    //   }
    // }
  },
  methods: {
    ...mapActions("room", ["updateRoomState", "changeRoomState"]),
    addCurrTemp(){
      // targetTemp = targetTemp+1;
      // this.$store
      this.$store.commit('room/setTargetTemp',this.roomState.targetTemp+1);
    },
    subCurrTemp(){
      // if(targetTemp>0)
      // targetTemp = targetTemp-1;
       this.$store.commit('room/setTargetTemp',this.roomState.targetTemp-1);
    }
  },
};
</script>

<style>
.user-panel {
  background-color: white;
  margin-top: 10px;
  padding: 10px;
  margin-left: 30%;
  margin-right: 30%;
}
</style>