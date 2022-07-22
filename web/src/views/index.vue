<template>
  <div class="Aiagain">
    <div v-if="!isload" id="loading">
      <FadeLoader class="aiagain-loading" color="#666"/>
      <p class="aiagain-loading-text">正在初始化,请稍后...</p>
    </div>
    <div
      v-else
      class="aiagain-wheel"
      v-bind:class="[!isload ? 'isload' : '']"
      v-bind:style="{backgroundImage:'url(' + starbg + ')'}"
    >
      <div v-if="!isStart" class="aiagain-title">
        <img :src="title" class="aiagain-title-img" alt=""/>
      </div>
      <Active v-if="isStart" ref="Active"/>
      <div
        v-if="!isStart"
        class="game-startBtn"
        v-bind:style="{backgroundImage:'url(' + startBtn + ')'}"
        @click="toStart"
      ></div>
    </div>
  </div>
</template>
<script>
import FadeLoader from "../packages/spinner/src/FadeLoader.vue";
import starbg from "../static/images/homeBg.png"
import title from "../static/images/title.png"
import startBtn from "../static/images/startBtn.png"

export default {
  components: {
    FadeLoader
  },
  data() {
    return {
      isload: false,
      isStart: false,
      active: null,
      starbg: starbg,
      title: title,
      startBtn: startBtn,
    };
  },
  computed: {},
  created() {
    this.isload = true
  },
  watch: {},
  methods: {
    toStart() {
      this.isStart = true
    },
  }
};
</script>
<style>
#loading {
  width: 100%;
  height: 100vh;
  justify-content: center;
  align-items: center;
  align-content: center;
  overflow: hidden;
  z-index: 9999;
}

.aiagain-loading {
  display: block;
  height: 30px;
  top: 200px !important;
  left: 48%;
  margin-bottom: 5px;
}

.aiagain-loading-text {
  width: 100%;
  line-height: 0.8rem;
  font-size: 0.3rem;
  color: #666;
  text-align: center;
  margin: 230px auto 0 auto;
}

.isload {
  opacity: 0;
}

.container {
  width: 100%;
}

.aiagain-wheel {
  width: 100%;
  height: 100vh;
  background-size: 100%;
  background: #c3c8c9 no-repeat;
  position: relative;
  overflow-x: hidden;
  overflow-y: auto;
}

.aiagain-title {
  width: 6.5rem;
  height: 4rem;
  background-size: 100%;
  margin: 0 auto;
  position: absolute;
  top: 16%;
  left: 0.5rem;
}

.aiagain-title-img {
  width: 100%;
  height: 100%;
}

.wheel-main {
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
  top: 2.7rem;
  left: 0;
}

.game-startBtn {
  width: 178px;
  height: 70px;
  display: block;
  background-size: 100% 100%;
  position: absolute;
  top: 80%;
  left: 50%;
  transform: translateX(-50%);
}
</style>

