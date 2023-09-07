import { getModule } from "vuex-module-decorators";
import { Store } from "vuex";

import AdminModule from "@/store/modules/admin";
import MainModule from "@/store/modules/main";

let adminStore: AdminModule;
let mainStore: MainModule;

// eslint-disable-next-line @typescript-eslint/no-explicit-any
function initializeStores(store: Store<any>): void {
  adminStore = getModule(AdminModule, store);
  mainStore = getModule(MainModule, store);
}

export const modules = {
  admin: AdminModule,
  main: MainModule,
};

export { initializeStores, adminStore, mainStore };
