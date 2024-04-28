<template>
  <div>
    <svg class="focus" viewBox="-50 -50 100 100">
      <line x1="-50" x2="50" y1="0" y2="0" stroke-width="5" stroke="black" />
      <line x1="0" x2="0" y1="50" y2="-50" stroke-width="5" stroke="black" />
    </svg>
  </div>
</template>

<script setup lang="ts"></script>

<style scoped>
.focus {
  position: fixed;
  left: calc(50vw - 50px);
  top: calc(50vh - 50px);
  width: 100px;
  height: 100px;
}
</style>
