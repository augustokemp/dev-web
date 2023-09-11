<template>
  <TemplateCard
    title="Criar Usuário"
    subtitle="Preencha as informações abaixo para criar um novo usuário"
  >
    <FormComponent
      title="Dados do Usuário"
      submitLabel="Adicionar usuário"
      :fields="fields"
    />
    <template #actions>
      <v-btn to="/main/users/" small rounded color="secondary">Lista</v-btn>
    </template>
  </TemplateCard>
</template>

<script lang="ts">
import TemplateCard from "@/components/TemplateCard.vue";
import FormComponent from "@/components/FormComponent.vue";
import Component from "vue-class-component";

@Component({
  components: {
    TemplateCard,
    FormComponent,
  },
})
export default class UsersCreate extends TemplateCard {
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
      password: true,
    },
    {
      label: "Endereço(s)",
      model: "addresses",
      type: "form",
      multiple: true,
      submitLabel: "Adicionar endereço",
      flat: true,
      clearOnSubmit: true,
      fields: [
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
      ],
    },
  ];

  switchMenu(open: boolean) {
    const el: any = this.$refs.MenuComponent;
    if (el) {
      el.isOpen = open;
    }
  }

  addAddress() {}
  //   this.formUser.data.addresses.push({
  //     street: this.formAddress.data.street,
  //     street_number: this.formAddress.data.street_number,
  //     neighborhood: this.formAddress.data.neighborhood,
  //     city: this.formAddress.data.city,
  //     uf: this.formAddress.data.uf,
  //   });

  //   this.formAddress.data.street = "";
  //   this.formAddress.data.street_number = "";
  //   this.formAddress.data.neighborhood = "";
  //   this.formAddress.data.city = "";
  //   this.formAddress.data.uf = "";

  //   this.switchMenu(false);

  //   const el: any = this.$refs.FormComponent;
  //   if (el) {
  //     el.resetValidation();
  //   }
  // }

  addUser() {}
}
</script>

<style>
</style>