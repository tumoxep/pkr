<template>
  <div class="game-bar">
    <TabbedView :tabs="gameBarTabs" :tabSetAction="'ui/gameBarSetTab'">
      <template v-if="gameBarTab === 'main'">
        <p>main</p>
      </template>
      <template v-else-if="gameBarTab === 'history'">
        <p>history</p>
      </template>
      <template v-else-if="gameBarTab === 'settings'">
        <p>settings</p>
      </template>
    </TabbedView>
  </div>
</template>

<script>
import { mapState } from 'vuex'
import TabbedView from '../views/Tabbed'

export default {
  name: 'GameBar',
  computed: {
    ...mapState('ui', ['gameBarTabs', 'gameBarTab'])
  },
  components: {
    TabbedView
  }
}
</script>

<style lang="scss" scoped>
@import '@/assets/styles/variables';

.game-bar {
  width: 100%;
  height: 270px;
}
</style>