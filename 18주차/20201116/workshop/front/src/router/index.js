import Vue from 'vue'
import VueRouter from 'vue-router'
import TodoList from '../views/TodoList'
import CreateTodo from '../views/CreateTodo'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'TodoList',
    component: TodoList,
  },
  {
    path: '/create',
    name: 'CreateTodo',
    component: CreateTodo,
  },
  
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
