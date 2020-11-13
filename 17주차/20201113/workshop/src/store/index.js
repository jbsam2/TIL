import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    todos: [
      {title:'입실체크', complete: false, id:1},
    ]
  },
  mutations: {
    UPDATE_TODO: function(state, todoItem){
      // state.todos.push(todoItem)
      state.todos = state.todos.map((todo)=>{
        if (todo.id === todoItem.id){
          return todoItem
        }
        else{
          return todo
        }
      })
    },
    ADD_TODO(state,todoTitle){
      const newTodo = {title: todoTitle, complete:false, id:Date.now()}
      state.todos.push(newTodo)
    },
  },
  actions: {
    // createTodo: function(context, todoItem){
    //   context.commit('CREATE_TODO',todoItem)
    // }
  },
})
