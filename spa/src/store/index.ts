import Vue from "vue";
import Vuex, { Store } from "vuex";
import { initializeStores, modules } from "@/utils/store-acessor";

Vue.use(Vuex);

// eslint-disable-next-line @typescript-eslint/no-explicit-any
const initializer = (store: Store<any>) => initializeStores(store);

export const plugins = [initializer];

export * from "@/utils/store-acessor";

export default new Store({
  plugins,
  modules,
});
