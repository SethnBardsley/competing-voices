<template>
  <div class="main-container">
    <div class="next-container">
      <div>
        <div class="question">
          On a scale of 1-5 how well could you understand the instructed speech?
        </div>
        <div class="buttons-row">
          <button
            :disbaled="loading"
            class="button-style"
            @click="$emit('tracking', 1)"
          >
            1
          </button>
          <button
            :disbaled="loading"
            class="button-style"
            @click="$emit('tracking', 2)"
          >
            2
          </button>
          <button
            :disbaled="loading"
            class="button-style"
            @click="$emit('tracking', 3)"
          >
            3
          </button>
          <button
            :disbaled="loading"
            class="button-style"
            @click="$emit('tracking', 4)"
          >
            4
          </button>
          <button
            :disbaled="loading"
            class="button-style"
            @click="$emit('tracking', 5)"
          >
            5
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
const props = defineProps<{
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
