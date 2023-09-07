<template>
  <div>
    <v-navigation-drawer
      v-model="showDrawer"
      persistent
      :mini-variant="miniDrawer"
      fixed
      app
      width="280"
      hide-overlay
    >
      <v-list nav dense class="drawer">
        <v-subheader> </v-subheader>
        <v-list-item to="/main/dashboard">
          <v-list-item-action>
            <v-icon>mdi-laptop</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>Dashboard</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-list-item to="/main/profile/view">
          <v-list-item-action>
            <v-icon>mdi-account</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>Meu Usuário</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
      <v-divider></v-divider>

      <v-text-field
        flat
        clearable
        v-model.trim="searchTool"
        dense
        hide-details
        placeholder="Buscar módulo"
        filled
        color="primary"
      />

      <v-divider></v-divider>
    </v-navigation-drawer>

    <v-app-bar
      color="primary"
      flat
      app
      dense
      ref="main-toolbar"
      v-mutate="onMutateToolbar"
    >
      <v-app-bar-nav-icon
        :class="showDrawer ? '' : 'drawerMenu'"
        @click.stop="switchShowDrawer"
      ></v-app-bar-nav-icon>
      <!-- <v-toolbar-title v-text="appName"></v-toolbar-title> -->
      <!-- <v-toolbar-title
          :class="isMobile ? 'text-subtitle-2 align-self-center text-center px-0' : ''"
          >Olá <b>{{ currentUser.full_name }}</b
          >{{
            isMobile
              ? ""
              : currentUser.franchising_id === 1
              ? ", bem vindo ao KNN MASTER"
              : ", bem vindo ao PHENOM MASTER"
          }}</v-toolbar-title
        > -->

      <v-card-text class="white--text">{{ userName }} </v-card-text>

      <v-menu bottom left offset-y>
        <template v-slot:activator="{ on }">
          <v-btn icon v-on="on">
            <v-icon>mdi-dots-vertical</v-icon>
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

const routeGuardMain = async (to, _from, next) => {
  if (to.path === "/main") {
    next("/main/dashboard");
  } else {
    next();
  }
};

//@ts-ignore
@Component
export default class Main extends Vue {
  public appName = appName;

  public loadingUserTools = true;
  public tool_id = 0;
  public lastAccessedPath = "";
  public disableForwardButton = false;
  public disableBackButton = false;
  public keyOpen = "";
  openedExpansionPanel: number | null = null;

  searchTool = "";

  adminTools = [
    {
      path: "/main/admin/usuarios/all",
      name: "Usuários",
      icon: "mdi-account-group",
    },
    { path: "/main/tools/all", name: "Módulos", icon: "mdi-toolbox" },
    { path: "/main/roles/all", name: "Cargos", icon: "mdi-account-details" },
  ];

  get userName() {
    return this.currentUser.full_name;
  }

  public onMutateToolbar() {
    let height = 0;
    const toolbar = this.$refs["main-toolbar"];
    if (toolbar) {
      //@ts-ignore
      height = `${toolbar.$el.offsetHeight}px`;
      //@ts-ignore
      document.documentElement.style.setProperty("--toolbarHeight", height);
    }
  }

  public async beforeRouteEnter(to, from, next) {
    // await userToolStore.getUserToolsIndexed();
    routeGuardMain(to, from, next);
  }

  public beforeRouteUpdate(to, from, next) {
    // Auto-hide Drawer
    const pathsToHideDrawer: any[] = [];
    if (_.some(pathsToHideDrawer, (p) => _.includes(to.path.split("/"), p))) {
      this.showDrawer = false;
    }

    // Auto-show Drawer
    const pathsToShowDrawer: any = [];
    if (_.some(pathsToShowDrawer, (p) => p === to.path)) {
      this.showDrawer = true;
    }

    routeGuardMain(to, from, next);
    this.lastAccessedPath = to.fullPath;
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

  // get comunicadosImportantesNaoLidos() {
  //   return _.filter(communicateStore.communicatesUser, (value) => {
  //     if (!value.is_read && value.is_important) return value;
  //   });
  // }

  set showDrawer(value) {
    mainStore.setDashboardShowDrawer(value);
  }

  public switchShowDrawer() {
    mainStore.setDashboardShowDrawer(!mainStore.dashboardShowDrawer);
  }

  public switchMiniDrawer() {
    mainStore.setDashboardMiniDrawer(!mainStore.dashboardMiniDrawer);
  }

  public get hasAdminAccess() {
    return mainStore.hasAdminAccess;
  }

  public routerBack() {
    this.$router.back();
    this.disableBackButton =
      this.$router.currentRoute.fullPath === "/main/dashboard";
    this.disableForwardButton = false;
  }

  public routerGo() {
    this.$router.forward();
    this.disableBackButton = false;
    this.disableForwardButton =
      this.lastAccessedPath === this.$router.currentRoute.fullPath;
  }

  public routerRefresh() {
    document.location.reload();
  }

  // public showUnreadImportantsCommunicates() {
  //   let form: any = this.$refs.comunicados;
  //   form.show();
  // }

  beforeCreate() {
    const storageTheme = localStorage.getItem("darkThemeKNN");
    if (storageTheme) {
      this.$vuetify.theme.dark = true;
    } else {
      this.$vuetify.theme.dark = false;
    }
  }

  public async mounted() {}

  public async logout() {
    await mainStore.userLogOut();
  }
}
</script>
