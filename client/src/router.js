import { createRouter, createWebHistory } from 'vue-router';
import MainScreen from './components/MainScreen/MainScreen'
import NotFound from './components/NotFoundPage/NotFound' 

export const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/',
      name: 'MainScreen',
      component: MainScreen
    },
    {
      path: '/:catchAll(.*)',
      name: 'NotFound',
      component: NotFound
    }
  ]
})