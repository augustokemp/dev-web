<template>
  <v-data-table
    :hide-default-footer="hideDefaultFooter"
    :hide-default-header="hideDefaultHeader"
    :items-per-page="hideDefaultFooter ? -1 : undefined"
    :headers="headers"
    :items="items"
    :loading="loading"
    :loading-text="loadingText"
  >
    <template v-for="(x, slotName) in $scopedSlots" v-slot:[slotName]="context">
      <slot :name="slotName" v-bind="context" />
    </template>
  </v-data-table>
</template>

<script lang="ts">
import Component from "vue-class-component";
import { Prop } from "vue-property-decorator";
import Vue from "vue";

@Component
export default class DataTableComponent extends Vue {
  @Prop({ type: Array, default: () => [] }) readonly headers!: any[];
  @Prop({ type: Array, default: () => [] }) readonly items!: any[];
  @Prop({ type: Boolean, default: false }) readonly hideDefaultFooter!: boolean;
  @Prop({ type: Boolean, default: false }) readonly hideDefaultHeader!: boolean;
  @Prop({ type: Boolean, default: false }) readonly loading!: boolean;
  @Prop({ type: String, default: "Carregando informações..." })
  readonly loadingText!: boolean;
}
</script>

<style scoped>
</style>