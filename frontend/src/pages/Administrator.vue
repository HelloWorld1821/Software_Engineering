<!--
 * @Description: 
 * @Author: l
 * @Date: 2021-06-01 15:36:52
 * @LastEditors: l
 * @LastEditTime: 2021-06-25 23:54:46
 * @FilePath: \DistributedControlSystem\frontend\src\pages\Administrator.vue
-->
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

<el-tabs :tab-position="tabPosition" style="height:1000px">
    <el-tab-pane label="监视房间">
        <div class="content">
             <div class="rooms-table">
            <el-table :data="roomsState" border style="width: 100%" >
              <el-table-column prop="roomId" label="房间ID" width="160" >
              </el-table-column>
               <el-table-column prop="state" label="送风状态" width="160" >
              </el-table-column>
              <el-table-column prop="mode" label="空调模式" width="160">
              </el-table-column>
              <el-table-column prop="speed" label="当前风速" width="160"> 
              </el-table-column>
              <el-table-column prop="currTemp" label="当前温度" width="160"> 
              </el-table-column>
              <el-table-column prop="targetTemp" label="目标温度" width="" >
              </el-table-column>
            </el-table>
          </div>
        </div>
    </el-tab-pane>
    <el-tab-pane label="设置参数">
        <div class="content">

        </div>
    </el-tab-pane>
</el-tabs>
  </div>
</template>

<script>
import { mapActions, mapState } from "vuex";
export default {
  data: function () {
    return {
      tabPosition: 'left',
    };
  },
  computed: {
    ...mapState("administrator", ["roomsState", "stateIsOk"]),
  },
  methods: {
    ...mapActions("administrator", ["checkRoomsState","setDefaultParams"]),
  },
  mounted:function(){
    let that= this;
    that.checkRoomsState();
    if(this.timer){
      clearInterval(this.timer);
    }else{
      this.timer = setInterval(()=>{
          let that =this;
          that.checkRoomsState();
      },10000);
    }
  },
  destroyed:function(){
		 clearInterval(this.timer);
	}
};
</script>

<style >
.content {
  margin-top: 50px;
  margin-left: 10%;
  margin-right: 10%;
  background-color: pink;
}

</style>