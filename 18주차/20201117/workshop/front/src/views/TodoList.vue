<template>
  <div>
    <ul>
      <li v-for='todo in todos' :key="todo.id">
        <input type="checkbox" :checked='todo.completed' @change="updateTodo(todo)">
        <span @click="updateTodo(todo)" :class="{completed: todo.completed}">{{todo.content}}</span>
        <button @click="deleteTodo(todo.id)">X</button>
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios'
// const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  data(){
    return {
      todos:[],
    }
  },
  methods:{
    setToken(){
      const token = localStorage.getItem('jwt')
      const config = {
        headers: {
          Authorization: `JWT ${token}`
        }
      }
      return config
    },
    deleteTodo(id){
      const config = this.setToken()
      // 서버에 해당 todo 삭제하는 요청보내고
      // 삭제된 내용 화면에 반영
      axios({
        url: `http://127.0.0.1:8000/todos/${id}/`,
        method: 'DELETE',
        headers: config.headers,
      })
      .then((res) => {
        // todos 최신화 2가지-
        // 1. 서버에 todos 요청해서 갱신
        // 2. id가지고 todos 갱신
        console.log(res)
        this.todos = this.todos.filter((todo) => todo.id !== id)
        // const targetTodoIdx = this.todos.findIndex((todo) => {
        //     return todo.id === res.data.id
        // })
        // this.todos.splice(targetTodoIdx, 1)
      })
      .catch((err) => {
        console.log(err)
      })
    },
    updateTodo(todo){
      const config = this.setToken()
      axios({
        url: `http://127.0.0.1:8000/todos/${todo.id}/`,
        method: 'PUT',
        data: {
          ...todo,
          completed: !todo.completed,
        },
        headers: config.headers,
      })
      .then((res) => {
        todo.completed = res.data.completed
        console.log(res)
      })
      .catch((err) => {
        console.log(err)
      })
    }
  },
  created(){
    // todos를 api를 찔러서 가져와서
    // data의 todos에 할당해준다
    const config = this.setToken()
    axios({
      url: 'http://127.0.0.1:8000/todos/',
      method: 'GET',
      headers: config.headers,
    })
    .then(res => {
      console.log(res.data)
      this.todos = res.data
    })
    .catch(err => {
      console.log(err)
    })
  },
}
</script>

<style>
  .completed {
    text-decoration: line-through;
    color: rgb(112, 112, 112);
  }
</style>