<template>
  <v-container class="d-flex justify-center align-center" fluid>
    <v-card width="500" :class="{ loginCard: isLoading }">
      <v-card-text class="primary--text text-h6"> Login </v-card-text>
      <v-card-text class="text-right">
        <FormComponent
          :class="{ loginForm: isLoading }"
          class="rounded-lg pa-2"
          dense
          submitLabel="Entrar"
          :loading="isLoading"
          :key="1"
          flat
          ref="FormComponent"
          @submit="onSubmit"
          :fields="fields"
          auto-focus-first
          auto-reset
        />
      </v-card-text>
      <v-card-text class="grey--text font-italic">
        <v-row align="center" dense>
          <v-col class="mx-auto" cols="auto">
            Usuário Inicial:
            <v-chip @click="clipboardCopy(firstAdmin)" x-small label>
              {{ firstAdmin }}
            </v-chip>
            -
            <v-chip @click="clipboardCopy(firstAdminPassword)" x-small label>
              {{ firstAdminPassword }}
            </v-chip>
          </v-col>
        </v-row>
        <v-row align="center" dense>
          <v-col class="mx-auto text-caption" cols="auto">
            (Clique para copiar)
          </v-col>
        </v-row>
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

  get firstAdmin() {
    return process.env.VUE_APP_FIRST_SUPERUSER;
  }

  get firstAdminPassword() {
    return process.env.VUE_APP_FIRST_SUPERUSER_PASSWORD;
  }

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

  clipboardCopy(text: string) {
    const textarea = document.createElement("textarea");
    textarea.value = text;
    textarea.style.position = "fixed";
    textarea.style.opacity = "0";
    document.body.appendChild(textarea);
    textarea.select();
    document.execCommand("copy");
    document.body.removeChild(textarea);
    this.$swal({
      width: "230px",
      icon: "success",
      text: "Copiado para área de transferência",
      timer: 1000,
      showConfirmButton: false,
    });
  }

  async onSubmit(formData) {
    const { username, password } = formData;
    // const form: any = this.$refs.FormComponent;
    this.isLoading = true;
    // form.loading = true;
    setTimeout(async () => {
      await mainStore.logIn({
        username: username,
        password: password,
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

@keyframes moveGradient {
  0% {
    background-position: -100% 0%;
  }
  100% {
    background-position: 100% 0%;
  }
}

.loginCard {
  background: linear-gradient(to right, #d4d4d44f, #fff, #d4d4d44f);
  background-size: 200% 200%;
  animation: moveGradient 2s linear infinite;
}

.loginForm {
  background-color: #fff;
}
</style>