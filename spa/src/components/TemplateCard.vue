<template>
  <v-card class="ma-0 pa-0 ma-md-3 pa-md-3">
    <v-card-title v-if="title" class="primary--text">
      {{ title }}
      <v-spacer></v-spacer>
      <div>
        <slot name="actions" />
      </div>
    </v-card-title>
    <v-card-subtitle v-if="subtitle">
      {{ subtitle }}
    </v-card-subtitle>
    <v-card-text>
      <slot />
    </v-card-text>
  </v-card>
</template>

<script lang="ts">
import Component from "vue-class-component";
import { Prop } from "vue-property-decorator";
import Vue from "vue";
import { mainStore } from "@/store";

@Component
export default class TemplateCard extends Vue {
  @Prop({ type: String, default: "" }) readonly title!: string;
  @Prop({ type: String, default: "" }) readonly subtitle!: string;

  get currentUser() {
    return mainStore.userProfile!;
  }

  get currentUserTools() {
    return this.currentUser.user_tools;
  }
}
</script>

<style>
</style>