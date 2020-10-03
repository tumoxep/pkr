<template>
  <div class="card-table">
    <Card
      v-for="(card, index) in cards"
      :key="index"
      :cardValue="card.value"
      :cardType="card.type"
      :style="cardStyle(index)"
    />
  </div>
</template>

<script>
import Card from '../components/Card'

export default {
  name: 'CardTable',
  data() {
    return {
      innerWidth: window.innerWidth
    }
  },
  props: {
    cards: {
      type: Array
    }
  },
  methods: {
    onResize() {
      this.innerWidth = window.innerWidth
    }
  },
  computed: {
    cardStyle() {
      return (index) => {
        const width = this.innerWidth > 767 ? this.innerWidth - 340 : this.innerWidth;
        return {
          'z-index': index,
          'margin-right': `-${width > 750 ? 0 : (750 - width) / 4}px`
        }
      }
    },
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
    Card
  }
}
</script>

<style lang="scss" scoped>
.card-table {
  display: flex;
  position: relative;
}
</style>