<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <!-- 세번째: 보여준다 -->
    <HelloWorld msg="Welcome to Your Vue.js App"/>
    <!-- 하나하나가 컴포넌트 -->
    <HelloWorld msg="Welcome to Your Vue.js App"/>
    <HelloWorld msg="Welcome to Your Vue.js App"/>
  </div>
</template>

<script>
// 첫번째 : 불러온다
import HelloWorld from './components/HelloWorld.vue'

// 두번째 : 등록한다
export default {
  name: 'App',
  components: {
    HelloWorld
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
