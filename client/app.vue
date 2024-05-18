<template>
  <div v-if="experiment" class="app">
    <div v-if="display === 'next'" class="main-container">
      <div v-if="experiment" class="options">
        Trial:
        <input v-model="trialNumber" />
        / {{ experiment.trials.length }}
      </div>
      <div class="next-container">
        <button
          v-if="experiment && startButton"
          class="button-style"
          @click="beginTrial"
        >
          Begin Trial
        </button>
        <div v-else>Please Wait</div>
      </div>
    </div>
    <Focus v-if="display === 'focus' || display === 'prompt'" />
    <TrialQuestion
      v-if="display === 'question' && trial"
      :question="trial.question"
      :loading="loading"
      @answer="answerQuestion"
    />
    <TrialPrompt v-if="display === 'prompt' && trial" :trial="trial" />
    <End v-if="display === 'end'" />
  </div>
  <div v-else class="app">
    <Next v-if="display === 'next'" />
  </div>
  <div v-else>Waiting For Server</div>
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

export type Display = "next" | "focus" | "question" | "prompt" | "end";

const display = ref<Display>("next");
const experiment = ref<Experiment | null>(null);
const trialNumber = ref<string>("1");
const loading = ref(false);
const startButton = ref(false);

const retrieveExperiment = async () => {
  try {
    experiment.value = (await $axios.get<Experiment>("/experiment")).data;
  } catch (e) {
    setTimeout(() => {
      retrieveExperiment();
    }, 1000);
  }
};

onMounted(() => {
  retrieveExperiment();
});

const trial = computed(() =>
  experiment.value &&
  experiment.value.trials.length + 1 > parseInt(trialNumber.value)
    ? experiment.value?.trials[parseInt(trialNumber.value) - 1]
    : null
);

const beginTrial = async () => {
  display.value = "prompt";
  await new Promise((resolve) => {
    setTimeout(() => {
      resolve(true);
    }, 5000);
  });
  display.value = "focus";
  await await $axios.get<Experiment>(`/start-trial/${trial.value?.key}`);
  await new Promise((resolve) => {
    setTimeout(() => {
      resolve(true);
    }, 1000);
    display.value = "question";
  });
};

const answerQuestion = async (answer: Answer) => {
  loading.value = true;
  await await $axios.get<Experiment>(
    `/answer-question/${trial.value?.key}/${answer.key}`
  );
  loading.value = false;
  trialNumber.value = String(parseInt(trialNumber.value) + 1);
  if (parseInt(trialNumber.value) > (experiment.value?.trials.length || 0)) {
    display.value = "end";
  } else {
    display.value = "next";
    startButton.value = false;
    setTimeout(() => {
      startButton.value = true;
    }, 15000);
  }
};
</script>

<style scoped>
.app {
  width: 100vw;
  height: 100vh;
  margin: -8px;
}

.options {
  position: absolute;
  left: 40px;
  top: 40px;
}

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
}

.button-style:hover {
  background-color: #eeeeee;
}

.button-style:active {
  background-color: #dddddd;
}
</style>
