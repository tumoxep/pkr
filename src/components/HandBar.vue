<template>
  <div class="hand-bar">
    <TabbedView :tabs="handBarTabs" :tabSetAction="'ui/handBarSetTab'">
      <template v-if="handBarTab === 'fold'">
        <p>main</p>
      </template>
      <template v-else-if="handBarTab === 'check'">
        <p>check</p>
      </template>
      <template v-else-if="handBarTab === 'call'">
        <p>call</p>
      </template>
      <template v-else-if="handBarTab === 'raise'">
        <p>raise</p>
      </template>
    </TabbedView>
  </div>
</template>

<script>
import { mapState } from 'vuex'
import TabbedView from '../views/Tabbed'

export default {
  name: 'HandBar',
  computed: {
    ...mapState('ui', ['handBarTabs', 'handBarTab'])
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