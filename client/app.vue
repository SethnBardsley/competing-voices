<template>
  <div v-if="experiment" class="app">
    <Next v-if="display === 'next'" />
    <Focus v-if="display === 'focus' || display === 'prompt'" />
    <TrialQuestion v-if="display === 'question'" />
    <TrialPrompt v-if="display === 'prompt'" />
  </div>
  <div v-else class="app">
    <Next v-if="display === 'next'" />
  </div>
</template>

<script setup lang="ts">
import type { Experiment, Question, Trial, Answer } from "./types";
import axios from "axios";

const $axios = axios.create({
  baseURL: "http://localhost:5001",
  headers: {
    common: {},
  },
});

export type Display = "next" | "focus" | "question" | "prompt";

const display = ref<Display>("next");
const experiment = ref<Experiment | null>(null);
const trialIndex = ref<number>(0);

onMounted(async () => {
  experiment.value = (await $axios.get<Experiment>("/experiment")).data;
});
</script>

<style scoped>
.app {
  width: 100vw;
  height: 100vh;
  margin: -8px;
}
</style>
