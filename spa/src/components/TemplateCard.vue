<template>
  <v-card class="ma-0 pa-0 ma-md-3 pa-md-3">
    <v-card-title v-if="title" class="primary--text">
      {{ title }}
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

@Component
export default class TemplateCard extends Vue {
  @Prop({ type: String, default: "" }) readonly title!: string;
  @Prop({ type: String, default: "" }) readonly subtitle!: string;
}
</script>

<style>
</style>