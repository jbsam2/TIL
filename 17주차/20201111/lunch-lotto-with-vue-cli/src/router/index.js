import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import TheLunch from '../views/TheLunch.vue'
import TheLotto from '../views/TheLotto.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/', // 경로를 적어주는 곳
    name: 'Home',
    component: Home // 경로에 적힌곳을 보여주는 부분
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  },
  {
    path: '/lunch', // 경로를 적어주는 곳
    name: 'TheLunch',
    component: TheLunch // 경로에 적힌곳을 보여주는 부분
  },
  {
    path: '/lotto', // 경로를 적어주는 곳
    name: 'TheLotto',
    component: TheLotto // 경로에 적힌곳을 보여주는 부분
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
