<template>
  <div class="game-page" ref="Game" v-bind:style="{backgroundImage: 'url(' + backGround + ')'}">
  </div>
</template>

<script>
import game from './game';
import backGround from '@/static/images/bg.png'

export default {
  name: 'Active',
  data(){
    return {
      layer: true,
      layer2: false,
      backGround: backGround
    }
  },
  computed: {
  },
  mounted(){
    game.gameInit(this.$refs.Game, this.$comm);
  },
  methods:{}
}
</script>
<style>
canvas{
  width: 100%;
  position: absolute;
  left: 0;
  top: 0;
}
</style>
