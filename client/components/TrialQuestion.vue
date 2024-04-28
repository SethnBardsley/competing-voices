<template>
  <div></div>
</template>

<script setup lang="ts">
import type { Question, Answer } from "../types.ts";
const props = defineProps<{
  question: Question;
}>();
</script>

<style scoped>
.button-style {
  background-color: #f4f4f4f4;
  border-radius: 4px;
  padding: 16px;
  font-size: 24px;
}

.button-style:hover {
  background-color: #eeeeee;
}

.button-style:active {
  background-color: #dddddd;
}
</style>
