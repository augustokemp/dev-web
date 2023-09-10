<template>
  <div>
    <v-app-bar clipped-left color="primary" app>
      <v-app-bar-nav-icon @click.stop="switchShowDrawer">
        <v-icon color="white">mdi-menu</v-icon>
      </v-app-bar-nav-icon>
      <v-card-text class="white--text">{{ userName }} </v-card-text>

      <v-menu bottom left offset-y>
        <template v-slot:activator="{ on }">
          <v-btn icon v-on="on">
            <v-icon color="white">mdi-dots-vertical</v-icon>
          </v-btn>
        </template>

        <v-list>
          <v-list-item to="/main/profile">
            <v-list-item-content>
              <v-list-item-title>Meu usuário</v-list-item-title>
            </v-list-item-content>
            <v-list-item-action>
              <v-icon>mdi-account</v-icon>
            </v-list-item-action>
          </v-list-item>
          <v-list-item @click="logout">
            <v-list-item-content>
              <v-list-item-title>Sair</v-list-item-title>
            </v-list-item-content>
            <v-list-item-action>
              <v-icon>mdi-close</v-icon>
            </v-list-item-action>
          </v-list-item>
        </v-list>
      </v-menu>
    </v-app-bar>

    <v-navigation-drawer clipped v-model="showDrawer" app>
      <v-list nav dense class="drawer">
        <v-subheader>
          <span class="blink mr-2">></span>
          Dev Web APP
        </v-subheader>
        <v-list-item to="/main/home">
          <v-list-item-action>
            <v-icon>mdi-laptop</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>Home</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
      <v-divider></v-divider>
      <v-divider></v-divider>
    </v-navigation-drawer>

    <v-main>
      <router-view></router-view>
    </v-main>
  </div>
</template>
  
  <script lang="ts">
import { appName } from "@/env";
import { mainStore } from "@/utils/store-acessor";
import _ from "lodash";
import { Component, Vue } from "vue-property-decorator";

//@ts-ignore
@Component
export default class Main extends Vue {
  public appName = appName;

  get userName() {
    return this.currentUser.full_name;
  }

  public getPath(module: string, isAdminTool: boolean) {
    const modulePath = module
      .normalize("NFD")
      .replace(/[^a-zA-Zs]/g, "")
      .toLowerCase();
    if (isAdminTool) return `/main/admin/${modulePath}`;
    return `/main/${modulePath}`;
  }

  get miniDrawer() {
    return mainStore.dashboardMiniDrawer;
  }

  get currentUser() {
    return mainStore.userProfile!;
  }

  public fixedTools = [];

  get showDrawer() {
    return mainStore.dashboardShowDrawer;
  }

  set showDrawer(value) {
    mainStore.setDashboardShowDrawer(value);
  }

  public switchShowDrawer() {
    mainStore.setDashboardShowDrawer(!mainStore.dashboardShowDrawer);
  }

  public get hasAdminAccess() {
    return mainStore.hasAdminAccess;
  }

  public routerRefresh() {
    document.location.reload();
  }

  public async mounted() {}

  public async logout() {
    await mainStore.userLogOut();
  }
}
</script>
