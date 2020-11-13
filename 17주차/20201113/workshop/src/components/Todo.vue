<template>
  <div><input type="checkbox" :checked='todo.complete' @change="onChange">{{ todo.title }}</div>
</template>

<script>
export default {
  name: 'Todo',
  props: {
    todo: Object,
  },
  methods: {
    onChange(){
      this.$store.commit('UPDATE_TODO',{        
        // title: this.todo.title,
        // complete: !this.todo.complete,
        // id: this.todo.id,
        ...this.todo,
        complete:!this.todo.complete
      })
    }
  }
}
</script>

<style>

</style>