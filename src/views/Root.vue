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
.action-button {
  position: absolute;
  bottom: 20px;
  right: 20px;
  z-index: 10;
}
</style>
