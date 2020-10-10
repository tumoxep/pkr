<template>
  <div class="hand-bar">
    <TabbedView :tabId="'handBar'">
      <template v-if="activeTab === 'fold'">
        <Checkbox :value="isFoldAny">fold any</Checkbox>
      </template>
      <template v-else-if="activeTab === 'check'">
        <Checkbox :value="isAutoCheck">auto check/fold</Checkbox>
      </template>
      <template v-else-if="activeTab === 'call'">
        <Checkbox :value="isCallAny">call any</Checkbox>
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
import Checkbox from '../components/Checkbox'

export default {
  name: 'HandBar',
  data() {
    return {
      isFoldAny: false,
      isAutoCheck: false,
      isCallAny: false
    }
  },
  props: ['cards'],
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
    TabbedView,
    Card,
    Checkbox
  }
}
</script>

<style lang="scss" scoped>
@import '@/assets/styles/constants';
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
.checkbox {
  margin-top: 10px;
}
</style>
