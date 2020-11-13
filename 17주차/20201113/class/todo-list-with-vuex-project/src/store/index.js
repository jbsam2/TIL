import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from 'vuex-persistedstate'

Vue.use(Vuex)

export default new Vuex.Store({
  state: { // 상태
    todos: []
  },
  getters: { //계산된 값 data를 변경하지 않음 (state 변화 ㄴㄴ)
    allTodosCnt: function(state){
      return state.todos.length
    },
    completedTodosCnt: function(state){
      return state.todos.filter((todo) => {
        return todo.completed === true
      }).length
    },
    uncompletedTodosCnt: function(state){
      return state.todos.filter((todo) => {
        return todo.completed === false
      }).length
    },
  },
  mutations: { // state를 변경하는 로직 (반드시 동기적으로 작성)
    CREATE_TODO: function(state, todoItem){
      // console.log(state)
      // console.log(todoItem)
      state.todos.push(todoItem)
    },
    DELETE_TODO: function(state, todoItem){
      const idx = state.todos.indexOf(todoItem)
      state.todos.splice(idx, 1)
    },
    UPDATE_TODO: function(state, todoItem){
      // 1. todos 배열을 반복하며
      state.todos = state.todos.map((todo)=>{
        // 2. 꺼낸 요소와 넘어온 요소가 같으면 실행 여부만 바꿔서 반환
        if (todo === todoItem){
          return {
            // title: todoItem.title,
            // completed: !todo.completed,
            ...todo,
            completed: !todo.completed,
          }
        }
        // 3. 같지 않다면 그대로 넘김
        return todo
      })
    },
  },
  actions: { // 모든 로직이 다포함 외부 data를 가져오고 가공하는 다양한일이 가능
    createTodo: function({commit}, todoItem){
      // console.log('createTodo from actions')
      // console.log(context)
      // context.commit('CREATE_TODO',todoItem)
      commit('CREATE_TODO',todoItem)
    },
    deleteTodo: function({commit}, todoItem){
      // console.log(context,todoItem)
      commit('DELETE_TODO',todoItem)
    },
    updateTodo:function({commit}, todoItem){
      commit('UPDATE_TODO',todoItem)
    },
  },
  plugins: [
    createPersistedState(),
  ]
})
