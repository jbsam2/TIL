<template>
  <div>
    <h1>Login</h1>
    <div>
      <label for="username">username: </label>
      <input type="text" id='username' v-model="credentials.username">
    </div>
    <div>
      <label for="password">password: </label>
      <input
        type="password"
        id='password'
        v-model="credentials.password"
        @keypress.enter="login"
      >
    </div>
    <button @click="login">Login</button>
  </div>
</template>

<script>
import axios from 'axios'


export default {
  name: 'Login',
  data: function () {
    return {
      credentials: {
        username: '',
        password: '',
      }
    }
  },
  methods: {
    login: function () {
      axios({
        url: `http://127.0.0.1:8000/accounts/api-token-auth/`,
        method: 'POST',
        data: this.credentials,
      })
      .then((res) => {
        localStorage.setItem('jwt', res.data.token)
        this.$emit('login')
        this.$router.push({name:'TodoList'})
      })
      .catch((err) => {
        console.log(err)
      })
    }
  }
}
</script>