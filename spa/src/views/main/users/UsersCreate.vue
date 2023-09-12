<template>
  <TemplateCard
    title="Criar Usuário"
    subtitle="Preencha as informações abaixo para criar um novo usuário"
  >
    <FormComponent
      ref="FormComponent"
      @submit="onSubmit"
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
import { adminStore, toolStore } from "@/store";
import _ from "lodash";

@Component({
  components: {
    TemplateCard,
    FormComponent,
  },
})
export default class UsersCreate extends TemplateCard {
  get fields() {
    return [
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
        label: "Administrador",
        model: "is_admin",
        type: "boolean",
        outlined: true,
        filled: true,
        dense: true,
        rounded: true,
        required: false,
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
      {
        label: "Módulos",
        model: "user_tools",
        type: "form",
        key: "tool_id",
        multiple: true,
        submitLabel: "Adicionar módulo",
        flat: true,
        clearOnSubmit: false,
        fields: this.toolFields,
      },
    ];
  }

  switchMenu(open: boolean) {
    const el: any = this.$refs.MenuComponent;
    if (el) {
      el.isOpen = open;
    }
  }

  get toolFields() {
    return _.map(this.tools, (t) => {
      return {
        id: t.id,
        label: t.name,
        multiboolean: true,
        model: "tool_id",
        type: "multiboolean",
        items: [
          {
            label: "ID",
            model: "tool_id",
            type: "text",
            value: t.id,
            required: false,
            readonly: true,
            filled: true,
            outlined: true,
            dense: true,
            hideDetails: true,
          },
          {
            label: "Criar",
            model: "allow_create",
            type: "boolean",
            required: false,
          },
          {
            label: "Ler",
            model: "allow_read",
            type: "boolean",
            required: false,
          },
          {
            label: "Atualizar",
            model: "allow_update",
            type: "boolean",
            required: false,
          },
          {
            label: "Deletar",
            model: "allow_delete",
            type: "boolean",
            required: false,
          },
        ],
      };
    });
  }

  get tools() {
    return toolStore.tools;
  }

  onSubmit(val) {
    console.log(val);
  }

  async mounted() {
    const params = _.get(this.$router.currentRoute, "params", {});
    const id = _.get(params, "id");

    if (id) {
      await adminStore.getUser(id);
      const user = adminStore.user;
      const form: any = this.$refs.FormComponent;
      if (form) {
        form.formData = user;
      }
    }

    await toolStore.getTools();
  }
}
</script>

<style>
</style>