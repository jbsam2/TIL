<template>
  <form @submit="onSubmit">
    <input type="text" v-model.trim="content">
    <button>추가하기</button>
  </form>
</template>

<script>
import axios from 'axios'

export default {
  data(){
    return{
      content: '',
    }
  },
  methods: {
    setToken: function(){
      const token = localStorage.getItem('jwt')
      const config = {
        headers: {
          Authorization: `JWT ${token}`
        }
      }
      return config
    },
    onSubmit(event){
      const config = this.setToken()
      event.preventDefault()
      // data의 content를 우리 api 서버에 요청한다 post axios로 
      // 잘 보내졌으면? todolist로 페이지 이동
      const todoItem = {
        content: this.content,
      }
      if (todoItem.content){
        axios({
          url: 'http://127.0.0.1:8000/todos/',
          method: 'POST',
          data: {
            content: this.content,
          },
          headers: config.headers,
        })
        .then(() => {
          this.$router.push({ name: 'TodoList' })
        })
        .catch(err => {
          console.log(err)
        })
      }      
    },
  },
}
</script>

<style>

</style>