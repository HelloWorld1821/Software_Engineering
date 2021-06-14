<!--
 * @Description: 
 * @Author: l
 * @Date: 2021-06-01 15:36:52
 * @LastEditors: l
 * @LastEditTime: 2021-06-14 15:29:16
 * @FilePath: \DistributedControlSystem\frontend\src\pages\Administrator.vue
-->
<template>
  <div>
    <h2>Admistrator</h2>
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

    </div>
  </div>
</template>

<script>
import { mapActions, mapState } from "vuex";
export default {
  data: function () {
    return {

    };
  },
  computed: {
    ...mapState("administrator", ["roomsState", "stateIsOk"]),
  },
  methods: {
    ...mapActions("administrator", ["checkRoomsState","setDefaultParams"]),
  },
  mounted:function(){
    // console.log("do it ...")
    // console.log("checkRoomsState...");
    let that= this;
    that.checkRoomsState();
    if(this.timer){
      clearInterval(this.timer);
    }else{
      this.timer = setInterval(()=>{
          // console.log("do it ...")
          // console.log("checkRoomsState...");
          let that =this;
          that.checkRoomsState();
      },1000);
    }
  },
  destroyed:function(){
		 clearInterval(this.timer);
	}
};
</script>

<style>
.rooms-state-div {
  margin-left: 20%;
  background-color: white;
  margin-right: 20%;
  margin-top: 10px;
}

</style>