<template>
  <div class="main-container">
    <div class="next-container">
      <div>
        <div class="question">{{ question.question }}</div>
        <div class="prompt">
          {{ question.prompt.replace("_", "_".repeat(10)) }}
        </div>
        <div class="buttons-row">
          <button
            v-for="answer in question.answers"
            :disbaled="loading"
            class="button-style"
            @click="$emit('answer', answer)"
          >
            {{ answer.text }}
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import type { Question, Answer } from "../types.ts";
const props = defineProps<{
  question: Question;
  loading: boolean;
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

.button-style {
  background-color: #f4f4f4f4;
  border-radius: 4px;
  padding: 16px;
  font-size: 24px;
  margin: 16px;
}

.buttons-row {
  display: flex;
}
.question {
  font-size: 24px;
  padding: 16px;
  font-weight: bold;
}

.prompt {
  font-size: 24px;
  padding: 16px;
}

.button-style:hover {
  background-color: #eeeeee;
}

.button-style:active {
  background-color: #dddddd;
}
</style>
