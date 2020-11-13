<template>
  <div>
    <div>
      <span :class='{done:todo.completed}' @click="updateTodo">{{ todo.title }}</span>
    </div>
    <button @click="deleteTodo">Del</button>
  </div>
</template>

<script>
export default {
  name: 'Todo',
  props: {
    todo: Object,
  },
  methods: {
    deleteTodo: function(){
      this.$store.dispatch('deleteTodo',this.todo)
    },
    updateTodo: function(){
      this.$store.dispatch('updateTodo',this.todo)
    }
  }
}
</script>

<style scoped>
  .done{
    text-decoration: line-through;
    color: grey;
  }
</style>