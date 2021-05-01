<template>
  <div id="app">
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App',
  components: {
  }
}
</script>

<style>
html, body {
  margin:0;
  scroll-behavior: smooth;
}

body {
  overflow-x: hidden;
  -ms-overflow-style: none;  /* IE and Edge */
  scrollbar-width: none;/* Firefox */
}

body::-webkit-scrollbar {
    display: none;
}

#app {
  overflow-x: hidden;
  -ms-overflow-style: none;  /* IE and Edge */
  scrollbar-width: none;/* Firefox */
}


#app::-webkit-scrollbar {
    display: none;
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  overflow-x: hidden;
}
</style>
