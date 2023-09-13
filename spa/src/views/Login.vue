<template>
  <v-container class="d-flex justify-center align-center" fluid>
    <v-card width="500">
      <v-card-text class="primary--text text-h6"> Login </v-card-text>
      <v-card-text class="text-right">
        <FormComponent
          :loading="isLoading"
          :key="1"
          flat
          ref="FormComponent"
          @submit="onSubmit"
          :fields="fields"
        />
      </v-card-text>
    </v-card>
  </v-container>
</template>

<script lang="ts">
import { mainStore } from "@/store";
import Vue from "vue";
import Component from "vue-class-component";
import FormComponent from "@/components/FormComponent.vue";

@Component({
  components: { FormComponent },
})
export default class Login extends Vue {
  isValid = false;
  isLoading = false;

  username = "admin@dev-web.com";
  password = "devweb123";

  get fields() {
    return [
      {
        type: "text",
        disabled: this.isLoading,
        outlined: true,
        dense: true,
        filled: true,
        rounded: true,
        color: "primary",
        model: "username",
        required: true,
        label: "E-mail",
      },
      {
        label: "Senha",
        disabled: this.isLoading,
        model: "password",
        type: "password",
        outlined: true,
        filled: true,
        dense: true,
        rounded: true,
        required: true,
        password: true,
      },
    ];
  }

  reset() {
    this.username = "";
    this.password = "";
  }

  async onSubmit() {
    // const form: any = this.$refs.FormComponent;
    this.isLoading = true;
    // form.loading = true;
    setTimeout(async () => {
      await mainStore.logIn({
        username: this.username,
        password: this.password,
      });
      this.isLoading = false;
    }, 1000);
    // form.loading = false;
  }
}
</script>

<style scoped>
.container {
  background-color: var(--v-light);
  position: relative;
  height: 100vh;
}
</style>