import Vue from 'vue'
import Router from 'vue-router'
import ListEquations from '@/components/ListEquations'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/equations',
      name: 'ListEquations',
      component: ListEquations
    }
  ],
  mode: 'history'
})
