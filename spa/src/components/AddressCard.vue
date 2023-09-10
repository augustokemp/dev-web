<template>
  <v-card max-width="fit-content">
    <v-tooltip bottom>
      <template #activator="{ on, attrs }">
        <v-btn
          v-on="on"
          v-bind="attrs"
          small
          @click="onCloseClick"
          icon
          class="closeBtn"
        >
          <v-icon>mdi-close</v-icon>
        </v-btn>
      </template>
      <span> Remover </span>
    </v-tooltip>
    <v-list two-line dense>
      <v-list-item v-for="(value, key) in content" :key="key">
        <v-list-item-content>
          <v-list-item-title>
            {{ key }}
          </v-list-item-title>
          <v-list-item-subtitle>
            {{ value }}
          </v-list-item-subtitle>
        </v-list-item-content>
      </v-list-item>
    </v-list>
  </v-card>
</template>

<script lang="ts">
import Component from "vue-class-component";
import Vue from "vue";
import { Emit, Prop } from "vue-property-decorator";

@Component
export default class AddressCard extends Vue {
  @Prop({ type: Object }) readonly content!: any;

  @Emit("close")
  onCloseClick() {
    return true;
  }
}
</script>

<style scoped>
::v-deep .closeBtn {
  position: absolute;
  top: 10px;
  right: 5px;
  z-index: 10;
}
</style>