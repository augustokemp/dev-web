<template>
  <TemplateCard
    title="Criar Usuário"
    subtitle="Preencha as informações abaixo para criar um novo usuário"
  >
    <FormComponent lazy-validation v-model="formUser" :fields="fields">
      <template #custom-1>
        <div class="pa-3">
          Endereços

          <div v-if="formUser.data.addresses.length === 0" class="error--text">
            * Adicione ao menos 1 endereço.
          </div>
          <div v-else class="d-flex">
            <AddressCard
              @close="onClose(idx)"
              :class="idx === 0 ? 'ma-3 ml-0' : 'ma-3'"
              v-for="(address, idx) in formUser.data.addresses"
              :content="{
                Rua: `${address.street}, ${address.street_number} - ${address.neighborhood}`,
                Cidade: `${address.city} - ${address.uf}`,
              }"
              :key="idx"
            />
          </div>

          <v-btn small text color="secondary" @click="showFormAddress = true"
            >Adicionar novo endereço</v-btn
          >

          <FormComponent
            v-if="showFormAddress"
            class="mt-3"
            v-model="formAddress"
            :fields="fieldsAddress"
            ref="FormComponent"
          >
            <template #buttons>
              <v-btn
                text
                small
                color="secondary"
                rounded
                class="ma-3"
                :disabled="!formAddress.isValid"
                @click="addAddress"
                >Adicionar Endereço</v-btn
              >
              <v-btn text small color="primary" @click="showFormAddress = false"
                >Cancelar</v-btn
              >
            </template>
          </FormComponent>
        </div>
      </template>
    </FormComponent>
    <template #actions>
      <v-btn to="/main/users/" small rounded color="secondary">Lista</v-btn>
    </template>
  </TemplateCard>
</template>

<script lang="ts">
import TemplateCard from "@/components/TemplateCard.vue";
import FormComponent from "@/components/FormComponent.vue";
import AddressCard from "@/components/AddressCard.vue";
import { IAddress } from "@/interfaces/address";
import { IUserProfileCreate } from "@/interfaces/userProfile";
import Component from "vue-class-component";

interface IFormUser {
  isValid: boolean;
  data: IUserProfileCreate;
}

interface IFormAddress {
  isValid: boolean;
  data: IAddress;
}

@Component({
  components: {
    TemplateCard,
    FormComponent,
    AddressCard,
  },
})
export default class UsersCreate extends TemplateCard {
  formUser: IFormUser = {
    isValid: false,
    data: {
      full_name: "",
      email: "",
      password: "",
      confirmPassword: "",
      is_active: true,
      is_admin: false,
      addresses: [],
    },
  };

  formAddress: IFormAddress = {
    isValid: false,
    data: {
      street: "",
      street_number: "",
      neighborhood: "",
      city: "",
      uf: "",
    },
  };

  showFormAddress = false;

  fields = [
    {
      label: "Nome completo",
      model: "full_name",
      type: "text",
      outlined: true,
      filled: true,
      dense: true,
      rounded: true,
      required: true,
      rules: [
        (v: string) =>
          (!!v && this.fullNameTest(v)) || "Digite seu nome completo",
      ],
    },
    {
      label: "E-mail",
      model: "email",
      type: "text",
      outlined: true,
      filled: true,
      dense: true,
      rounded: true,
      required: true,
      rules: [(v: string) => (!!v && this.emailTest(v)) || "E-mail inválido"],
    },
    {
      label: "Senha",
      model: "password",
      type: "password",
      outlined: true,
      filled: true,
      dense: true,
      rounded: true,
      required: true,
      password: true,
    },
    {
      label: "Confirmar senha",
      model: "confirm_password",
      type: "password",
      outlined: true,
      filled: true,
      dense: true,
      rounded: true,
      required: true,
      rules: [
        (v: string) =>
          (!!v && v === this.formUser.data.password) ||
          "A confirmação de senha precisa ser idêntica à senha",
      ],
      password: true,
    },
    {
      label: "Endereço(s)",
      model: "addresses",
      type: "custom-1",
      rules: [
        this.formUser.data.addresses.length > 0 ||
          "Adicione ao menos um endereço",
      ],
    },
  ];

  fieldsAddress = [
    {
      label: "Logradouro",
      model: "street",
      type: "text",
      outlined: true,
      filled: true,
      dense: true,
      rounded: true,
      required: true,
    },
    {
      label: "Número",
      model: "street_number",
      type: "text",
      outlined: true,
      filled: true,
      dense: true,
      rounded: true,
      required: true,
    },
    {
      label: "Bairro",
      model: "neighborhood",
      type: "text",
      outlined: true,
      filled: true,
      dense: true,
      rounded: true,
      required: true,
    },
    {
      label: "Cidade",
      model: "city",
      type: "text",
      outlined: true,
      filled: true,
      dense: true,
      rounded: true,
      required: true,
    },
    {
      label: "UF",
      model: "uf",
      type: "text",
      outlined: true,
      filled: true,
      dense: true,
      rounded: true,
      required: true,
    },
  ];

  onClose(index: number) {
    this.formUser.data.addresses.splice(index, 1);
  }

  addAddress() {
    this.formUser.data.addresses.push({
      street: this.formAddress.data.street,
      street_number: this.formAddress.data.street_number,
      neighborhood: this.formAddress.data.neighborhood,
      city: this.formAddress.data.city,
      uf: this.formAddress.data.uf,
    });

    this.formAddress.data.street = "";
    this.formAddress.data.street_number = "";
    this.formAddress.data.neighborhood = "";
    this.formAddress.data.city = "";
    this.formAddress.data.uf = "";

    this.showFormAddress = false;

    const el: any = this.$refs.FormComponent;
    if (el) {
      el.resetValidation();
    }
  }
}
</script>

<style>
</style>