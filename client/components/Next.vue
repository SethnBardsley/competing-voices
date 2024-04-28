<template>
  <div class="next-container">
    <button class="button-style">Begin Trial</button>
  </div>
</template>

<script setup lang="ts"></script>

<style scoped>
.next-container {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
  height: 100%;
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
