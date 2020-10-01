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
  props: {
    cardValue: {
      type: String
    },
    cardType: {
      type: String
    }
  },
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
@import '@/assets/styles/icomoon';

.card {
  width: 150px;
  height: 270px;
  background-color: #4a6572;
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
    background-color: #232f34;
    border-radius: 22px;
  }
  p {
    position: absolute;
    top: 0;
    left: 0;
    margin-top: 10px;
    margin-left: 10px;
    margin-bottom: 0;
    font-family: Arial, Helvetica, sans-serif;
    font-size: 20px;
    font-weight: bold;
    color: white;
    &::after {
      position: absolute;
      top: 0;
      left: 0;
      margin-top: 30px;
      margin-bottom: 0;
      font-family: icomoon;
      font-size: 20px;
      color: white;     
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