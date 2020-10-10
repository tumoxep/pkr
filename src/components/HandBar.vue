<template>
  <div class="hand-bar">
    <TabbedView :tabId="'handBar'">
      <template v-if="activeTab === 'fold'">
        <p>fold</p>
      </template>
      <template v-else-if="activeTab === 'check'">
        <p>check</p>
      </template>
      <template v-else-if="activeTab === 'call'">
        <p>call</p>
      </template>
      <template v-else-if="activeTab === 'raise'">
        <p>raise</p>
      </template>
    </TabbedView>
    <div class="card-table">
      <Card
        v-for="(card, index) in cards"
        :key="index"
        :cardValue="card.value"
        :cardType="card.type"
        :style="cardStyle(index)"
      />
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import TabbedView from '../views/Tabbed'
import Card from '../components/Card'

export default {
  name: 'HandBar',
  props: {
    cards: {
      type: Array
    }
  },
  computed: {
    ...mapGetters('ui', { activeTab: 'activeHandBarTab' }),
    cardStyle() {
      return index => {
        return {
          'z-index': index
        }
      }
    },
  },
  components: {
    Card,
    TabbedView
  }
}
</script>

<style lang="scss" scoped>
@import '@/assets/styles/variables';

.hand-bar {
  width: 100%;
  height: 400px;
  background-color: $main-color-2;
  border-radius: 22px;
  max-width: 340px;
  .tabbed-view {
    min-height: 140px;
  }
}
.card-table {
  float: center;
  display: flex;
  position: relative;
  padding-left: 10px;
}
</style>