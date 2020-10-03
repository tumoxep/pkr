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
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import TabbedView from '../views/Tabbed'

export default {
  name: 'HandBar',
  computed: {
    ...mapGetters('ui', { activeTab: 'activeHandBarTab' })
  },
  components: {
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
}
</style>