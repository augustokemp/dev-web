<template>
  <TemplateCard title="Usuários" subtitle="Lista de Usuários cadastrados">
    <DataTableComponent
      :loading="isLoading"
      loadingText="Carregando usuários..."
      hide-default-footer
      :items="users"
      :headers="headers"
    >
      <template #[`item.addresses`]="{ value, index }">
        <DataTableComponent
          :hide-default-header="index > 0"
          hide-default-footer
          :headers="headersAddresses"
          :items="value"
        >
          <template #[`item.city`]="{ item }">
            {{ item.city }} - {{ item.uf }}
          </template>
        </DataTableComponent>
      </template>
    </DataTableComponent>

    <template #actions>
      <v-btn to="/main/users/create" small rounded color="secondary"
        >Criar Usuário</v-btn
      >
    </template>
  </TemplateCard>
</template>

<script lang="ts">
import Component from "vue-class-component";
import TemplateCard from "@/components/TemplateCard.vue";
import DataTableComponent from "@/components/DataTableComponent.vue";
import { adminStore } from "@/store";

@Component({
  components: {
    TemplateCard,
    DataTableComponent,
  },
})
export default class UsersList extends TemplateCard {
  headers = [
    { text: "Nome", value: "full_name", align: "center" },
    { text: "E-mail", value: "email", align: "center" },
    { text: "Endereços", value: "addresses", align: "center" },
  ];

  headersAddresses = [
    { text: "Rua", value: "street", align: "center", sortable: false },
    {
      text: "Número",
      value: "street_number",
      align: "center",
      sortable: false,
    },
    { text: "Bairro", value: "neighborhood", align: "center", sortable: false },
    { text: "Cidade", value: "city", align: "center", sortable: false },
  ];

  isLoading = false;

  get users() {
    return adminStore.users;
  }

  async mounted() {
    this.isLoading = true;
    await adminStore.getUsers();
    this.isLoading = false;
  }
}
</script>

<style>
</style>