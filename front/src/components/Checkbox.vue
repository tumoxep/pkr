<template>
  <label class="checkbox">
    <span class="checkbox__input">
      <input
        type="checkbox"
        v-bind="$attrs"
        v-bind:value="value"
        @change="$emit('input', $event.target.value)"
      >
      <span class="checkbox__control">
        <svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' aria-hidden="true" focusable="false">
          <path fill='none' stroke='currentColor' stroke-width='3' d='M1.73 12.91l6.37 6.37L22.79 4.59' />
          <rect :fill="mainColor" width="24" height="24" x="0" y="0" rx="2" />
        </svg>
      </span>
    </span>
    <span class="radio__label">
      <slot></slot>
    </span>
  </label>
</template>

<script>
import themeMixin from '@/theme-mixin'

export default {
  name: 'ActionButton',
  mixins: [themeMixin],
  props: ['value']
}
</script>

<style lang="scss" src="@/assets/styles/checkbox.scss"></style>
