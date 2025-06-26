<script setup lang="ts">
const route = useRoute()
const paramId = computed(() => route.params.id)

const {data: note} = await useFetch(() => `/api/${paramId.value}`)
</script>

<template>
  <h1>Detail</h1>
  <NuxtLink to="/">Home Page</NuxtLink>
  <div>{{ note }}</div>
</template>