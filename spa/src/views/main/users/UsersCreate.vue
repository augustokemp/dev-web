<template>
  <TemplateCard
    title="Criar Usuário"
    subtitle="Preencha as informações abaixo para criar um novo usuário"
  >
    <FormComponent v-model="form" :fields="fields" />
    <template #actions>
      <v-btn to="/main/users/" small rounded color="secondary">Lista</v-btn>
    </template>
  </TemplateCard>
</template>

<script lang="ts">
import Component from "vue-class-component";
import TemplateCard from "@/components/TemplateCard.vue";
import FormComponent from "@/components/FormComponent.vue";

@Component({
  components: {
    TemplateCard,
    FormComponent,
  },
})
export default class UsersCreate extends TemplateCard {
  form = {
    isValid: false,
    data: {},
  };

  fields = [
    {
      label: "Nome completo",
      model: "full_name",
      type: "text",
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
      required: true,
      rules: [(v: string) => (!!v && this.emailTest(v)) || "E-mail inválido"],
    },
    {
      label: "Senha",
      model: "password",
      type: "password",
      required: true,
      password: true,
    },
    {
      label: "Confirmar senha",
      model: "confirm_password",
      type: "password",
      required: true,
      password: true,
    },
  ];
}
</script>

<style>
</style>