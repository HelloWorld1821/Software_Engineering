<!--
 * @Description: 
 * @Author: l
 * @Date: 2021-06-01 15:34:21
 * @LastEditors: l
 * @LastEditTime: 2021-06-14 15:31:55
 * @FilePath: \DistributedControlSystem\frontend\src\pages\Room.vue
-->
<template>
  <div>
    <h1>This is Room</h1>
    <div class="ac-control">
      <div class='temp-choose-div'>
        <h2 class="mb-0">AC Controller</h2>
        Target Temperature:
        <input type="button" @click="subCurrTemp" value="sub" />
        {{ targetTemp }}
        <input type="button" @click="addCurrTemp" value="add" />
      </div>
      <div class="speed-choose-div">
        Target Speed:
        <br>
        <input type="radio" value="low" id="low" v-model="targetSpeed" />
        <label for="low">Low</label>
        <br />
        <input type="radio" value="mid" id="mid" v-model="targetSpeed" />
        <label for="mid">Mid</label>
        <br />
        <input type="radio" value="high" id="high" v-model="targetSpeed" />
        <label for="high">High</label>
        <br />
        <span>Target Speed: {{ targetSpeed }}</span>
      </div>
      <div class='ac-state-choose-div'>
          AC State:
          <br>
          <input type="radio" value="on" id="on" v-model='targetACState'>
          <label for='on'>On</label>
          <br>
          <input type="radio" value="off" id="off" v-model="targetACState">
          <label for="off">Off</label>
          <br>
          <span>Target AC State: {{ targetACState }}</span>
          <br>
      </div>
      <div>
        <input type="button" value="update the Room State" @click='updateRoomState(roomId)'>
      </div>
    </div>
    <div class="user-panel">
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
    return {
      targetTemp: 20,
      targetSpeed: "low",
      targetACState: 'off',
    };
  },
  computed: {
    ...mapState("room", ["roomId", "roomState"]),
  },
  methods: {
    ...mapActions("room", ["updateRoomState", "changeRoomState"]),
    addCurrTemp() {
      this.targetTemp = this.targetTemp+1;
      
    },
    subCurrTemp() {
      if(this.targetTemp>0)
        this.targetTemp=this.targetTemp-1;
    },
    // 这个函数只是为了简化参数
    changeRoomStateHere(){
      this.changeRoomState(
        {targetTemp:this.targetTemp,
        targetSpeed:this.targetSpeed,
        targetACState:this.targetACState}
      )
    }
  },
  watch:{
    targetTemp:function(newValue,oldValue){
      console.log('targetTemp: '+oldValue+'-->'+newValue);
      this.$store.commit('room/setTargetTemp',newValue);
      this.changeRoomStateHere();
    },
    targetSpeed:function(newValue,oldValue){
      console.log('targetSpeed: '+oldValue+'-->'+newValue);
      this.changeRoomStateHere();
    },
    targetACState:function(newVaule,oldValue){
      console.log('targetACState: '+oldValue+'-->'+newVaule);
      this.changeRoomStateHere();
    }
  },
  mounted:function(){
    let that= this;
    that.updateRoomState(that.roomId);
    if(this.timer){
      clearInterval(this.timer);
    }else{
      this.timer = setInterval(()=>{
          let that =this;
          // that.checkRoomsState();
          that.updateRoomState(that.roomId);
      },1000);
    }
  },
  destroyed:function(){
		 clearInterval(this.timer);
	}
};
</script>

<style>
.user-panel {
  background-color: white;
  margin-top: 10px;
  margin-right: 20%;
  padding: 20px;
  /* display: inline-block; */
  float: right;
  width: 300px;
  height: 400px;
}
.ac-control {
  background-color: #fff;
  margin-top: 10px;
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
}
</style>