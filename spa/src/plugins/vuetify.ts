import Vue from "vue";
import Vuetify from "vuetify";

import pt from "vuetify/src/locale/pt";
import "vuetify/dist/vuetify.min.css";

Vue.use(Vuetify);

const opts = {
  lang: {
    locales: { pt },
    current: "pt",
  },
  theme: {
    dark: false,
    themes: {
      light: {
        primary: "#141E46",
        secondary: "#BB2525",
        accent: "#FF6969",
        light: "FFF5E0",
        "blue-accent": "#f2f7ff",
        "primary-light": "#F5F6FF",
        "grey-accent": "#99b2c6",
      },
    },
  },
};

export default new Vuetify(opts);
