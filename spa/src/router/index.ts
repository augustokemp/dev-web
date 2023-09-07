import Vue from "vue";
import Router from "vue-router";
// import { component } from "vue/types/umd";

// import RouterComponent from "../components/RouterComponent.vue";

Vue.use(Router);

export default new Router({
  mode: "history",
  base: process.env.BASE_URL,
  scrollBehavior() {
    return { x: 0, y: 0 };
  },
  routes: [
    {
      path: "/",
      name: "Start",
      component: () => import("../views/main/Start.vue"),
      children: [
        {
          path: "login",
          name: "login",
          component: () => import("../views/Login.vue"),
        },
        {
          path: "main",
          component: () => import("../views/main/Main.vue"),
          children: [
            {
              path: "home",
              component: () => import("../views/main/Home.vue"),
            },
          ],
        },
      ],
    },
    {
      path: "*",
      redirect: "/",
    },
  ],
});
