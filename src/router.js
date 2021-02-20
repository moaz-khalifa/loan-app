import Vue from 'vue'
import Router from 'vue-router'
import Loans from '@/components/Loans'
import Register from '@/components/Register'
import Login from '@/components/Login'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/loans',
      name: 'loans',
      component: Loans
    },
    {
      path: '/register',
      name: 'register',
      component: Register
    },
    {
      path: '/login',
      name: 'login',
      component: Login
    }
  ]
})
