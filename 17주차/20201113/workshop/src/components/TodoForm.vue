<template>
  <div>
    <input type="text" v-model="todoTitle" @keypress.enter="addTodo">
    <button @click="addTodo">Add</button>
  </div>
</template>

<script>
export default {
  name: 'TodoForm',
  data: function() {
    return {
      todoTitle: '',
    }
  },
  methods: {
    addTodo: function(){
      this.$store.commit('ADD_TODO', this.todoTitle)
      this.todoTitle = ''
    }
  }
}
</script>

<style>

</style>