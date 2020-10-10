<template>
  <div class="root-view">
    <GameBar />
    <CardTable :cards="tableCards" />
    <HandBar :cards="handCards"/>
    <ActionButton />
  </div>
</template>

<script>
import GameBar from '../components/GameBar'
import CardTable from '../components/CardTable'
import HandBar from '../components/HandBar'
import ActionButton from '../components/ActionButton'
import { mapActions } from 'vuex'

export default {
  name: 'RootView',
  data() {
    return {
      tableCards: [
        { value: '10', type: 'spades' },
        { value: '10', type: 'spades' },
        { value: '10', type: 'spades' },
        { value: '10', type: 'spades' },
        { value: '10', type: 'spades' }
      ],
      handCards: [
        { value: '10', type: 'spades' },
        { value: '10', type: 'spades' }
      ]      
    }
  },
  methods: {
    ...mapActions('ui', ['setInnerWidth']),
    onResize() {
      this.setInnerWidth(window.innerWidth)
    }
  },
  mounted() {
    this.$nextTick(() => {
      window.addEventListener('resize', this.onResize)
    })
  },
  beforeDestroy() { 
    window.removeEventListener('resize', this.onResize)
  },
  components: {
    GameBar,
    CardTable,
    HandBar,
    ActionButton
  }
}
</script>

<style lang="scss" scoped>
@import '@/assets/styles/constants';
.hand-bar {
  position: absolute;
  margin-bottom: -220px;
  @media (min-width: #{$breakpoint-mobile}) {
    margin-bottom: -70px;
  }
  bottom: 0;
  right: 0;
  z-index: 5;
}
.action-button {
  position: absolute;
  bottom: 20px;
  right: 20px;
  z-index: 10;
}
.game-bar {
  width: 100%;
  height: 240px;
  @media (min-width: #{$breakpoint-mobile}) {
    height: 640px;
  }
}
</style>
