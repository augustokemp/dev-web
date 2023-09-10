<template>
  <v-container class="d-flex justify-center align-center" fluid>
    <v-card width="500">
      <v-card-text class="primary--text text-h6"> Login </v-card-text>
      <v-card-text class="text-right">
        <v-form @submit.prevent="onSubmit" v-model="isValid">
          <v-text-field
            :disabled="isLoading"
            outlined
            dense
            filled
            rounded
            color="primary"
            v-model="username"
            :rules="[(v) => required(v, 'E-mail')]"
            label="E-mail"
          />
          <v-text-field
            :disabled="isLoading"
            outlined
            dense
            filled
            rounded
            color="primary"
            v-model="password"
            :rules="[(v) => required(v, 'Senha')]"
            label="Senha"
          />
          <v-btn :disabled="isLoading" @click="reset" text small>Limpar</v-btn>
          <v-btn
            :loading="isLoading"
            :disabled="!isValid"
            type="submit"
            text
            small
          >
            Acessar
          </v-btn>
        </v-form>
      </v-card-text>
    </v-card>
  </v-container>
</template>

<script lang="ts">
import { mainStore } from "@/store";
import Vue from "vue";
import Component from "vue-class-component";

@Component
export default class Login extends Vue {
  isValid = false;
  isLoading = false;

  username = "admin@dev-web.com";
  password = "devweb123";

  reset() {
    this.username = "";
    this.password = "";
  }

  async onSubmit() {
    this.isLoading = true;
    setTimeout(async () => {
      await mainStore.logIn({
        username: this.username,
        password: this.password,
      });
      this.isLoading = false;
    }, 1000);
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