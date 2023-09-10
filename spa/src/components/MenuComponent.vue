<template>
  <v-menu
    v-model="isOpen"
    :close-on-click="true"
    :close-on-content-click="closeOnClick"
    :offset-x="offset"
    :offset-y="offset"
  >
    <template #activator="{ on, attrs }">
      <div v-on="on" v-bind="attrs" style="max-width: fit-content">
        <slot name="activator">
          <v-btn small text>Abrir</v-btn>
        </slot>
      </div>
    </template>
    <v-card class="pa-3">
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
  </v-menu>
</template>

<script lang="ts">
import Component from "vue-class-component";
import Vue from "vue";
import { Prop } from "vue-property-decorator";

@Component
export default class MenuComponent extends Vue {
  @Prop({ type: Boolean, default: true }) readonly offset!: boolean;
  @Prop({ type: Boolean, default: false }) readonly closeOnClick!: boolean;
  @Prop({ type: String, default: "" }) readonly title!: string;
  @Prop({ type: String, default: "" }) readonly subtitle!: string;

  isOpen = false;
}
</script>

<style>
</style>