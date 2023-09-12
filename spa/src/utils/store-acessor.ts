import { getModule } from "vuex-module-decorators";
import { Store } from "vuex";

import AdminModule from "@/store/modules/admin";
import MainModule from "@/store/modules/main";
import ToolModule from "@/store/modules/tool";

let adminStore: AdminModule;
let mainStore: MainModule;
let toolStore: ToolModule;

// eslint-disable-next-line @typescript-eslint/no-explicit-any
function initializeStores(store: Store<any>): void {
  adminStore = getModule(AdminModule, store);
  mainStore = getModule(MainModule, store);
  toolStore = getModule(ToolModule, store);
}

export const modules = {
  admin: AdminModule,
  main: MainModule,
  tool: ToolModule,
};

export {
  initializeStores,
  adminStore,
  mainStore,
  toolStore,
};
