<template>
  <div id="app">
    <div id="nav">
      <!-- 라우터 링크는 새로고침 없이 이어준다. -->
      <router-link to="/">Home</router-link> |
      <router-link to="/about">About</router-link> |
      <router-link to="/lunch">TheLunch</router-link> |
      <router-link to="/lotto">TheLotto</router-link> |
    </div>
    <router-view/> <!-- Home 컴포넌트가 보여준곳/ 컴포넌트에 맞는걸 보여주는 부분이다. -->
  </div>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
