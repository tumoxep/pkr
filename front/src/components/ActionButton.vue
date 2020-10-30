<template>
  <button class="action-button"></button>
</template>

<script>
export default {
  name: 'ActionButton',
}
</script>

<style lang="scss" scoped>
@import '@/assets/styles/constants';
@import '@/assets/styles/icomoon';
.action-button {
  &::before {
    content: '\ea10';
    font-family: icomoon;
  }
  font-size: 20px;
  color: $main-color-3;
  background-color: #f9aa33;
  border: none;
  border-radius: 50%;
  width: 80px;
  height: 80px;
  @media (min-width: #{$breakpoint-mobile}) {
    width: 120px;
    height: 120px;
    font-size: 32px;
  }
}
</style>
