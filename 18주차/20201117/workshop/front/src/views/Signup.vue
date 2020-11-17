<template>
  <div>
    <h1>Signup</h1>
    <div>
      <label for="username">username: </label>
      <input type="text" id='username' v-model="credentials.username">
    </div>
    <div>
      <label for="password">password: </label>
      <input type="password" id='password' v-model="credentials.password">
    </div>
    <div>
      <label for="passwordConfirmation">password 확인: </label>
      <input
        type="password"
        id='passwordConfirmation'
        v-model="credentials.passwordConfirmation"
        @keypress.enter='signup'
      >
    </div>
    <button @click="signup">Signup</button>
  </div>
</template>

<script>
import axios from 'axios'


export default {
  name: 'Signup',
  data: function () {
    return {
      credentials: {
        username: '',
        password: '',
        passwordConfirmation: '',
      }
    }
  },
  methods: {
    signup: function () {
      axios({
        url: 'http://127.0.0.1:8000/accounts/signup/',
        method: 'POST',
        data: this.credentials,
      })
      .then((res)=>{
        console.log(res)
        this.$router.push({name:'Login'})
      })
      .catch((err)=>{
        console.log(err)
      })
    }
  }
}
</script>