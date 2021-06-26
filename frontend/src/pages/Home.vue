<!--
 * @Description: 
 * @Author: l
 * @Date: 2021-06-01 09:39:42
 * @LastEditors: l
 * @LastEditTime: 2021-06-26 21:57:46
 * @FilePath: \DistributedControlSystem\frontend\src\pages\Home.vue
-->

<template>
  <div>
    <el-carousel :interval="4000" type="card" height="200px">
      <el-carousel-item v-for="item in imageData" :key="item">
        <!-- <h3 class="medium">{{ item }}</h3>
         -->
        <img
          ref="imgHeight"
          :src="item.src"
          width="100%"
          height="100%"
          object-fit="cover"
        />
      </el-carousel-item>
    </el-carousel>
  </div>
</template>

<script>
export default {
  data: function () {
    return {
      bannerH: 300,
      imgData: [
        // {
        //   src: require("frontend\\src\\assets\\images\\003.jpg"),
        // },
        // {
        //   src: require("frontend\\src\\assets\\images\\003.jpg"),
        // },
        // {
        //   src: require("frontend\\src\\assets\\images\\003.jpg"),
        // },
        // {
        //   src: require("frontend\\src\\assets\\images\\003.jpg"),
        // },
        // {
        //  src: require("frontend\\src\\assets\\images\\003.jpg"),
        // },
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
.el-carousel__item h3 {
  margin-top: 100px;
  color: #475669;
  font-size: 14px;
  opacity: 0.75;
  line-height: 200px;
  margin: 0;
}

.el-carousel__item:nth-child(2n) {
  background-color: #99a9bf;
}

.el-carousel__item:nth-child(2n + 1) {
  background-color: #d3dce6;
}
</style>