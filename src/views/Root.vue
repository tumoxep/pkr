<template>
  <div id="root-view">
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
.hand-bar {
  position: absolute;
  bottom: -170px;
  left: 0;
  z-index: 5;
}
</style>