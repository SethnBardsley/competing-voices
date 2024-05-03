<template>
  <div class="main-container">
    <div class="next-container">
      <div>
        <div class="prompt">{{ trial.instructions }}</div>
      </div>
    </div>
    <svg
      v-if="trial.attend_position === 'left'"
      class="left-arrow"
      viewBox="0 0 60 20"
    >
      <rect x="10" y="5" width="50" height="10" fill="black" />
      <path d="M 0 10 L 10 0 L10 20 " fill="black" />
    </svg>
    <svg
      v-if="trial.attend_position === 'right'"
      class="right-arrow"
      viewBox="0 0 60 20"
    >
      <rect x="0" y="5" width="50" height="10" fill="black" />
      <path d="M 60 10 L 50 0 L 50 20 " fill="black" />
    </svg>
  </div>
</template>

<script setup lang="ts">
import type { Trial } from "../types.ts";
const props = defineProps<{
  trial: Trial;
}>();
</script>

<style scoped>
.main-container {
  width: 100%;
  height: 100%;
}
.next-container {
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}

.prompt {
  font-size: 24px;
  padding: 16px;
  transform: translateY(100px);
}

.left-arrow {
  position: absolute;
  left: 50px;
  top: 50vh;
  width: 60px;
}
.right-arrow {
  position: absolute;
  right: 50px;
  top: 50vh;
  width: 60px;
}
</style>
