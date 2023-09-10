<template>
  <v-form
    ref="Form"
    :lazy-validation="lazyValidation"
    :class="formClass"
    v-model="value.isValid"
  >
    {{ customRules }}aaa
    <template v-for="(field, idx) in fields">
      <v-text-field
        @blur="onBlur(field)"
        v-model="value.data[field.model]"
        :type="field.type"
        :outlined="field.outlined"
        :rounded="field.rounded"
        :filled="field.filled"
        :dense="field.dense"
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
      <slot v-else-if="field.type.startsWith('custom')" :name="field.type" />
    </template>
    <slot name="buttons" />
  </v-form>
</template>

<script lang="ts">
import Component from "vue-class-component";
import Vue from "vue";
import { Prop } from "vue-property-decorator";
import _ from "lodash";

@Component
export default class FormComponent extends Vue {
  @Prop({ type: Array }) readonly fields!: any[];
  @Prop({ type: Object }) readonly value!: any;
  @Prop({ type: Boolean, default: false }) readonly flat!: boolean;
  @Prop({ type: Boolean, default: false }) readonly lazyValidation!: boolean;

  get customRules() {
    console.log(_.flatMap(this.customFields, "rules"));
    return _.every(_.flatMap(this.customFields, "rules"));
  }

  get customFields() {
    return _.filter(this.fields, (f) => f.type.startsWith("custom"));
  }

  get formClass() {
    switch (true) {
      case this.flat:
        return "pa-3";
      default:
        return "pa-3 rounded-lg elevation-1";
    }
  }

  resetValidation() {
    const el: any = this.$refs.Form;
    if (el) {
      el.reset();
    }
  }

  onBlur(field: any) {
    if (field.password) {
      const el: any = this.$refs.Form;
      if (el) {
        el.validate();
      }
    }
  }
}
</script>

<style>
</style>