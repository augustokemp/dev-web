<template>
  <v-form v-model="value.isValid">
    <template v-for="(field, idx) in fields">
      <v-text-field
        v-model="value.data[field.model]"
        :type="field.type"
        :key="idx"
        v-if="['text', 'password'].includes(field.type)"
        :label="field.label"
        :rules="
          required
            ? [(v) => required(v, field.label), ...(field.rules || [])]
            : field.rules
        "
      >
        <template #append>
          <v-btn
            @click="
              field.type = field.type === 'password' ? 'text' : 'password'
            "
            icon
            v-if="field.password"
          >
            <v-icon v-if="field.type === 'password'">mdi-eye-off</v-icon>
            <v-icon v-else>mdi-eye</v-icon>
          </v-btn>
        </template>
      </v-text-field>
    </template>
  </v-form>
</template>

<script lang="ts">
import Component from "vue-class-component";
import Vue from "vue";
import { Prop } from "vue-property-decorator";

@Component
export default class FormComponent extends Vue {
  @Prop({ type: Array }) readonly fields!: any[];
  @Prop({ type: Object }) readonly value!: any;
}
</script>

<style>
</style>