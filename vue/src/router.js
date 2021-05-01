import Vue from 'vue';
import Router from 'vue-router';
import HelloWorld from './components/HelloWorld.vue';
import Home from './components/Home.vue';
import Prediction from './components/Prediction.vue';
import Library from './components/Library.vue';
import LibraryDisease from "./components/LibraryDisease.vue";

Vue.use(Router);

export default new Router({
    mode: 'history',
    base: process.env.BASE_URL,
    routes: [
      {
        path: '/hello',
        name: 'HelloWorld',
        component: HelloWorld,
      },
      {
        path: '/',
        name: 'Home',
        component: Home,
      },
      {
        path: '/prediction',
        name: 'Prediction',
        component: Prediction,
      },
      {
        path: '/library',
        name: 'Library',
        component: Library,
      },
      {
        path: "/library/:librarydisease",
        name:'LibraryDisease',
        component: LibraryDisease,
      }
    ],
  });
  