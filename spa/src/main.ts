import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import vuetify from "./plugins/vuetify";
import "./component-hooks";
import "./registerServiceWorker";
import { parse } from "date-fns";
import _ from "lodash";

Vue.config.productionTip = false;

new Vue({
  router,
  store,
  vuetify,
  render: (h) => h(App),
}).$mount("#app");

Vue.mixin({
  methods: {
    parseDate: function (date: string) {
      return parse(
        _.replace(date, /\D/g, "").slice(0, 8),
        "yyyyMMdd",
        new Date()
      );
    },
  },
  computed: {
    required: () => [(v) => !!v || "Campo obrigatório"],
  },
});

declare module "vue/types/vue" {
  interface Vue {
    parseDate(date: string): Date;
    required: () => any[];
    mixinPhoneRule: () => any[];
    mixinDateRules: () => any[];
  }
}
