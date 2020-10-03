<template>
  <div class="root-view">
    <GameBar />
    <CardTable :cards="cards" />
    <HandBar />
  </div>
</template>

<script>
import GameBar from '../components/GameBar'
import CardTable from '../components/CardTable'
import HandBar from '../components/HandBar'

export default {
  name: 'RootView',
  data() {
    return {
      cards: [
        { value: '10', type: 'spades' },
        { value: '10', type: 'spades' },
        { value: '10', type: 'spades' },
        { value: '10', type: 'spades' },
        { value: '10', type: 'spades' }
      ]
    }
  },
  components: {
    GameBar,
    CardTable,
    HandBar
  }
}
</script>

<style lang="scss" scoped>
@import '@/assets/styles/variables';
.hand-bar {
  position: absolute;
  margin-bottom: -170px;
  @media (min-width: #{$breakpoint-mobile}) {
    margin-bottom: 0;
  }
  bottom: 0;
  right: 0;
  z-index: 5;
}
.card-table {
  @media (min-width: #{$breakpoint-mobile}) {
    position: absolute;
    left: 0;
    bottom: 0;
  }
}
</style>
