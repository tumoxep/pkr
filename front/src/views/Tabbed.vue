<template>
  <div class="tabbed-view">
    <ul class="header">
      <li
        class="header-item"
        v-for="(tab, index) in tabs"
        :key="index"
        :class="headerItemClass(tab)"
      >
        <button class="header-item--button" @click="onClick(tab)">
          {{ tab.title }}
        </button>
      </li>
    </ul>
    <slot></slot>
  </div>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  name: "TabbedView",
  props: ["tabId"],
  computed: {
    ...mapGetters("ui", ["tabsById"]),
    tabs() {
      return this.tabsById(this.tabId);
    },
  },
  methods: {
    onClick(tab) {
      this.$store.dispatch("ui/setTab", { tab, tabId: this.tabId });
    },
    headerItemClass(tab) {
      return {
        "is-active": tab.active,
      };
    },
  },
};
</script>

<style lang="scss" scoped>
@import "@/assets/styles/constants";
.tabbed-view {
  padding-top: 10px;
  padding-left: 10px;
  .header {
    display: flex;
    margin: 0;
    padding-left: 0;
    list-style-type: none;
  }
  .header-item {
    .header-item--button {
      border: none;
      background: none;
      color: $main-color;
      font-size: 18px;
      padding: 10px;
      border-radius: 8px;
    }
    &.is-active {
      .header-item--button {
        background-color: $main-color;
        color: $main-color-2;
      }
    }
  }
}
</style>
