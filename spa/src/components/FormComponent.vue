<template>
  <v-card :flat="flat">
    <v-card-title class="primary--text text-subtitle-1" v-if="title">
      {{ title }}
    </v-card-title>
    <v-card-text>
      <v-form ref="Form" :lazy-validation="lazyValidation" v-model="isValid">
        <template v-for="(field, idx) in fields">
          <v-text-field
            v-if="['text', 'password'].includes(field.type)"
            @blur="onBlur(field)"
            v-model="formData[field.model]"
            :type="field.type"
            :outlined="field.outlined"
            :rounded="field.rounded"
            :filled="field.filled"
            :dense="field.dense"
            :key="idx"
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

          <v-card v-else-if="field.type === 'form'" :key="idx">
            <v-card-title class="text-subtitle-1">{{
              field.label
            }}</v-card-title>
            <v-card-text v-if="!settingParentField && formData[field.model]">
              {{ formData[field.model] }}
            </v-card-text>
            <v-card-text>
              <MenuComponent ref="MenuComponent" title="Adicionar endereço">
                <template #activator>
                  <v-btn small text color="secondary">Adicionar endereço</v-btn>
                </template>

                <template>
                  <FormComponent
                    @submitChild="(val) => updateParentField(val, field)"
                    :flat="field.flat"
                    :submit-label="field.submitLabel"
                    :fields="field.fields"
                    :isChild="true"
                    :clear-on-submit="field.clearOnSubmit"
                  />
                </template>
              </MenuComponent>
            </v-card-text>
          </v-card>

          <slot
            v-else-if="field.type.startsWith('custom')"
            :name="field.type"
          />
        </template>
        <slot name="buttons" />
      </v-form>
    </v-card-text>
    <v-card-actions class="mx-2">
      <v-btn
        class="ma-2 ml-0"
        :disabled="!isValid"
        rounded
        small
        color="primary"
        @click="isChild ? onSubmitChild() : onSubmit()"
        >{{ submitLabel }}</v-btn
      >
      <v-btn @click="resetFields" class="ma-2" rounded small>{{
        resetLabel
      }}</v-btn>
    </v-card-actions>
  </v-card>
</template>

<script lang="ts">
import Component from "vue-class-component";
import Vue from "vue";
import { Prop } from "vue-property-decorator";
import AddressCard from "@/components/AddressCard.vue";
import MenuComponent from "@/components/MenuComponent.vue";

import _ from "lodash";

@Component({
  components: { FormComponent, AddressCard, MenuComponent },
})
export default class FormComponent extends Vue {
  @Prop({ type: Array }) readonly fields!: any[];
  @Prop({ type: String, default: "" }) readonly title!: string;
  @Prop({ type: String, default: "Enviar" }) readonly submitLabel!: string;
  @Prop({ type: String, default: "Resetar" }) readonly resetLabel!: string;
  @Prop({ type: Boolean, default: false }) readonly flat!: boolean;
  @Prop({ type: Boolean, default: false }) readonly lazyValidation!: boolean;
  @Prop({ type: Boolean, default: true }) readonly clearOnSubmit!: boolean;
  @Prop({ type: Boolean, default: false }) readonly isChild!: boolean;

  onSubmit() {
    this.$emit("submit", this.formData);
  }

  onSubmitChild() {
    if (this.isChild) {
      this.$emit("submitChild", this.formData);
      if (this.clearOnSubmit) {
        this.formData = {};
      }
    }
  }

  updateParentField(val, field) {
    this.settingParentField = true;
    if (field.multiple) {
      if (!this.formData[field.model]) {
        this.formData[field.model] = [];
      }
      this.$set(this.formData, field.model, [
        ...this.formData[field.model],
        val,
      ]);
    } else {
      this.formData[field.model] = val;
    }
    this.settingParentField = false;
  }

  isValid = false;
  formData: any = {};
  settingParentField = false;

  get customRules() {
    return _.every(_.flatMap(this.customFields, "rules"));
  }

  get customFields() {
    return _.filter(this.fields, (f) => f.type.startsWith("custom"));
  }

  resetFields() {
    const el: any = this.$refs.Form;
    if (el) {
      el.reset();
    }
  }

  resetValidation() {
    const el: any = this.$refs.Form;
    if (el) {
      el.resetValidation();
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

  startMultipleFields() {
    _.forEach(this.fields, (f) => {
      if (f.type === "form") {
        if (f.multiple) {
          this.formData[f.model] = [];
          console.log(this.formData);
        }
      }
    });
  }

  mounted() {
    this.startMultipleFields;
  }
}
</script>

<style>
</style>