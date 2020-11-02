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
        <p class="raise-value">{{ raiseValue }}</p>
        <vue-slider
          v-model="raiseValue"
          :width="'82%'"
          :height="2"
          :dotSize="28"
          :tooltip="'none'"
          :dotStyle="{ 'background-color': mainColor }"
        />
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
import { mapGetters } from "vuex";
import VueSlider from "vue-slider-component";
import themeMixin from "@/theme-mixin";
import TabbedView from "../views/Tabbed";
import Card from "../components/Card";
import Checkbox from "../components/Checkbox";

export default {
  name: "HandBar",
  mixins: [themeMixin],
  props: ["cards"],
  data() {
    return {
      isFoldAny: false,
      isAutoCheck: false,
      isCallAny: false,
      raiseValue: 0,
    };
  },
  computed: {
    ...mapGetters("ui", { activeTab: "activeHandBarTab" }),
    cardStyle() {
      return (index) => {
        return {
          "z-index": index,
        };
      };
    },
  },
  components: {
    VueSlider,
    TabbedView,
    Card,
    Checkbox,
  },
};
</script>

<style lang="scss" src="@/assets/styles/vue-slider-theme.scss"></style>
<style lang="scss" scoped>
@import "@/assets/styles/constants";
.hand-bar {
  width: 100%;
  height: 400px;
  background-color: $main-color-2;
  border-radius: 22px;
  border: 1px solid $main-color;
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
.raise-value {
  margin-top: 0;
  margin-bottom: 0;
  color: $main-color-3;
  font-family: $base-font-family;
  font-size: 40px;
  font-style: italic;
  font-weight: bold;
}
.vue-slider {
  margin-left: 14px;
}
</style>
