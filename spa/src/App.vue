<template>
  <div id="app">
    <v-app :style="cssProps">
      <v-main v-if="loggedIn === null">
        <v-container class="fill-height">
          <v-row align="center" justify="center">
            <v-col>
              <div class="text-xs-center" style="text-align: center">
                <div class="headline my-5">Carregando...</div>
                <v-progress-circular
                  size="100"
                  indeterminate
                  color="primary"
                ></v-progress-circular>
              </div>
            </v-col>
          </v-row>
        </v-container>
      </v-main>
      <router-view v-else />
    </v-app>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";
import { mainStore } from "@/store";

@Component
export default class App extends Vue {
  get loggedIn() {
    return mainStore.isLoggedIn;
  }

  get cssProps() {
    var themeColors = {};
    Object.keys(this.$vuetify.theme.themes.light).forEach((color) => {
      themeColors[`--v-${color}`] = this.$vuetify.theme.themes.light[color];
    });
    return themeColors;
  }

  public async created() {
    await mainStore.checkLoggedIn();
  }
}
</script>
<style scoped>
@keyframes blink {
  0% {
    opacity: 0;
  }
  100% {
    opacity: 1;
  }
}
::v-deep .blink {
  animation: blink 0.5s infinite alternate;
}
</style>