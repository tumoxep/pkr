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
import { mapState } from 'vuex'
import Card from '../components/Card'

export default {
  name: 'CardTable',
  props: ['cards'],
  computed: {
    ...mapState('ui', ['innerWidth']),
    cardStyle() {
      return index => {
        // this.innerWidth - 340 - после 767 учитывает HandBar 
        const width = this.innerWidth > 767 ? this.innerWidth - 340 : this.innerWidth
        return {
          // костыль отрисовки тени
          'z-index': index,
          // 150 * 5 = 750. Если контейнер меньше, докидываем каждой карте четверть разницы
          'margin-right': `-${width > 750 ? 0 : (750 - width) / 4 - 20}px`
        }
      }
    },
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
