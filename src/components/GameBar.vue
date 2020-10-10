<template>
  <div class="game-bar">
    <TabbedView :tabId="'gameBar'">
      <template v-if="activeTab === 'main'">
        <p>main</p>
      </template>
      <template v-else-if="activeTab === 'history'">
        <p>history</p>
      </template>
      <template v-else-if="activeTab === 'settings'">
        <p>settings</p>
      </template>
    </TabbedView>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import TabbedView from '../views/Tabbed'

export default {
  name: 'GameBar',
  computed: {
    ...mapGetters('ui', { activeTab: 'activeGameBarTab' })
  },
  components: {
    TabbedView
  }
}
</script>

<style lang="scss" scoped>
@import '@/assets/styles/constants';

.game-bar {
  width: 100%;
  height: 270px;
  @media (min-width: #{$breakpoint-mobile}) {
    height: 640px;
  }
}
</style>
