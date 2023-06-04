<template>
  <MainScreen />
</template>

<script>
import MainScreen from '@/components/MainScreen/MainScreen.vue'
export default {
  name: "App",
  components: {
    MainScreen
  },
};
</script>

<style>
html, body {
  height: 100%;
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
  height: 100%;
  overflow-y: auto;
}
</style>
