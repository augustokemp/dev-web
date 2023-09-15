import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import vuetify from "./plugins/vuetify";
import "@/plugins/sweet-alert";
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
  data() {
    return {
      swalDefaults: {
        showCancelButton: true,
        confirmButtonText: "OK",
        cancelButtonText: "Cancelar",
        reverseButtons: true,
      },
    };
  },
  methods: {
    parseDate: function (date: string) {
      return parse(
        _.replace(date, /\D/g, "").slice(0, 8),
        "yyyyMMdd",
        new Date()
      );
    },
    required: (v: string, name: string = "Campo") =>
      !!v || `${name} é um campo obrigatório`,
    emailTest: (v: string) =>
      RegExp(/^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$/).test(v),
    fullNameTest: (v: string) =>
      RegExp(/^[A-Za-zÀ-ÖØ-öø-ÿ\s'-]+ [A-Za-zÀ-ÖØ-öø-ÿ\s'-]+$/).test(v),
  },
  // computed: {
  //   required: () => [(v) => !!v || "Campo obrigatório"],
  // },
});

declare module "vue/types/vue" {
  interface Vue {
    parseDate(date: string): Date;
    required: (v: string, name: string) => any[];
    emailTest: (v: string) => boolean;
    fullNameTest: (v: string) => boolean;
    mixinPhoneRule: () => any[];
    mixinDateRules: () => any[];
    swalDefaults: any;
  }
}
