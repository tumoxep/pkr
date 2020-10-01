<template>
  <div id="root-view">
    <CardTable :cards="cards" />
  </div>
</template>

<script>
import CardTable from '../components/CardTable'

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
    CardTable
  }
}
</script>

<style lang="scss" scoped>
</style>