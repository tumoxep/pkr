<template>
  <div>
    <div class="card">
      <p :class="cardValueClass">{{ cardValue }}</p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Card',
  props: ['cardValue', 'cardType'],
  computed: {
    cardValueClass() {
      if (!this.cardType) {
        return ''
      }
      return `card--${this.cardType}`
    }
  }
}
</script>

<style lang="scss" scoped>
@import '@/assets/styles/constants';
@import '@/assets/styles/icomoon';
.card {
  width: 150px;
  height: 270px;
  background-color: $main-color;
  border-radius: 22px;
  position: relative;
  &::before {
    content: '';
    position: absolute;
    z-index: -1;
    width: 150px;
    height: 270px;
    top: 5px;
    left: -5px;
    background-color: $main-color-2;
    border-radius: 22px;
  }
  p {
    position: absolute;
    top: 0;
    left: 0;
    margin-top: 10px;
    margin-left: 10px;
    margin-bottom: 0;
    font-family: $base-font-family;
    font-size: 20px;
    font-weight: bold;
    color: $main-color-3;
    &::after {
      position: absolute;
      top: 0;
      left: 0;
      margin-top: 30px;
      margin-bottom: 0;
      font-family: icomoon;
      font-size: 20px;
      color: $main-color-3;     
    }
    &.card--spades {
      &::after {
        content: '\e917';
      }
    }
    &.card--clubs {
      &::after {
        content: '\e918';
      }
    }
    &.card--diamonds {
      &::after {
        content: '\e919';
      }
    }
    &.card--heart {
      &::after {
        content: '\e9da';
      }
    }
  }
}
</style>
