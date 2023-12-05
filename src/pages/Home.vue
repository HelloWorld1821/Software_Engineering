<!--
 * @Description: 
 * @Author: l
 * @Date: 2021-06-01 09:39:42
 * @LastEditors: l
 * @LastEditTime: 2021-06-27 09:33:18
 * @FilePath: \DistributedControlSystem\frontend\src\pages\Home.vue
-->

<template>
  <div class='content-div'>
    <el-row>
      <h2>Welcome to Kusa Hotel</h2>
    </el-row>
    <el-row style="margin-top:20px">
      <el-carousel :interval="4000" type="card" height="450px">
        <el-carousel-item v-for="item in imgData2" :key="item.id">
          <!-- <h3 class="medium">{{ item }}</h3>
         -->
          <img
            ref="imgHeight"
            :src="item.idView"
            width="100%"
            height="100%"
            object-fit="cover"
          />
        </el-carousel-item>
      </el-carousel> </el-row
    >>
    <!-- <el-row>
      <el-carousel :interval="4000" type="card" height="300px">
        <el-carousel-item v-for="item in imgData2" :key="item.id">
          <img :src="item.idView" class="image" />
        </el-carousel-item>
      </el-carousel>
    </el-row> -->
  </div>
</template>

<script>
export default {
  data: function () {
    return {
      bannerH: 300,
      imgData2: [
        { id: 0, idView: require("../assets/images/1.jpg") },
        { id: 1, idView: require("../assets/images/2.jpg") },
        { id: 2, idView: require("../assets/images/3.jpg") },
        { id: 3, idView: require("../assets/images/4.jpg") },
        { id: 4, idView: require("../assets/images/5.jpg") },
      ],
    };
  },
  methods: {
    setBannerH() {
      this.bannerH = document.body.clientWidth / 4;
    },
  },
  mounted: function () {
    window.addEventListener(
      "resize",
      () => {
        this.setBannerH();
      },
      false
    );
  },
};
</script>

<style scope>
.content-div{
  margin-top: 50px;
  margin-right: 5%;
  margin-left: 5%;
}
</style>