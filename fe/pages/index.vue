<script setup lang="ts">
const {data: notes} = await useFetch("/api")
</script>

<template>
  <div>
    <h1>Home page</h1>

    <div v-for="note in notes" :key="note">
      <NuxtLink :to="{ name: 'id', params: { id: note } }">{{ note }}</NuxtLink>
    </div>
  </div>
</template>
