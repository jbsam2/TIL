<template>
  <div id="app">
    <h1>TodoList</h1>
    <p>all: {{allTodosCnt}}</p>
    <p>done: {{completedTodosCnt}}</p>
    <p>Not yet: {{uncompletedTodosCnt}}</p>
    <TodoForm />
    <TodoList />    
  </div>
</template>

<script>
import {mapGetters} from 'vuex'
import TodoList from '@/components/TodoList'
import TodoForm from '@/components/TodoForm'

export default {
  name: 'App',
  components: {
    TodoList,
    TodoForm,
  },
  computed: {
    // completedTodosCnt: function(){
    //   return this.$store.getters.completedTodosCnt
    // },
    // uncompletedTodosCnt: function(){
    //   return this.$store.getters.uncompletedTodosCnt
    // },
    // allTodosCnt: function(){
    //   return this.$store.getters.allTodosCnt
    // },
    ...mapGetters([
      'allTodosCnt','completedTodosCnt','uncompletedTodosCnt'
    ])
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
