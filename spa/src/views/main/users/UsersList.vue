<template>
  <TemplateCard title="Usuários" subtitle="Lista de Usuários cadastrados">
    <DataTableComponent
      :loading="isLoading"
      loadingText="Carregando usuários..."
      hide-default-footer
      :items="users"
      :headers="headers"
    >
      <template #[`item.is_admin`]="{ value }">
        <span v-if="value">Sim</span>
        <span v-else>Não</span>
      </template>

      <template #[`item.addresses`]="{ value }">
        <DataTableComponent
          hide-default-footer
          :headers="headersAddresses"
          :items="value"
        >
          <template #[`item.city`]="{ item }">
            {{ item.city }} - {{ item.uf }}
          </template>
        </DataTableComponent>
      </template>
      <template #[`item.edit`]="{ item }">
        <v-btn
          :to="`/main/users/create/${item.id}`"
          :disabled="
            !userTool.allow_update &&
            currentUser.id !== item.id &&
            !currentUser.is_admin
          "
          icon
        >
          <v-icon>mdi-pencil</v-icon>
        </v-btn>
      </template>
      <template #[`item.delete`]="{ item }">
        <v-btn
          @click="confirmDelete(item)"
          :disabled="
            (!userTool.allow_delete && !currentUser.is_admin) ||
            item.is_admin ||
            item.id === currentUser.id
          "
          icon
        >
          <v-icon>mdi-close</v-icon>
        </v-btn>
      </template>
    </DataTableComponent>

    <template #actions>
      <v-btn
        :disabled="!userTool.allow_create && !currentUser.is_admin"
        to="/main/users/create"
        small
        rounded
        color="secondary"
        >Criar Usuário</v-btn
      >
    </template>
  </TemplateCard>
</template>

<script lang="ts">
import Component from "vue-class-component";
import TemplateCard from "@/components/TemplateCard.vue";
import DataTableComponent from "@/components/DataTableComponent.vue";
import { adminStore, mainStore } from "@/store";
import _ from "lodash";
import { IUserProfile } from "@/interfaces/userProfile";

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
    { text: "Admin", value: "is_admin", align: "center" },
    { text: "Endereços", value: "addresses", align: "center", width: "50%" },
    { text: "Editar", width: 50, value: "edit", align: "center" },
    { text: "Excluir", width: 50, value: "delete", align: "center" },
  ];

  headersAddresses = [
    {
      text: "Rua",
      value: "street",
      align: "center",
      sortable: false,
      width: "25%",
    },
    {
      text: "Número",
      value: "street_number",
      align: "center",
      sortable: false,
      width: "15%",
    },
    {
      text: "Bairro",
      value: "neighborhood",
      align: "center",
      sortable: false,
      width: "35%",
    },
    {
      text: "Cidade",
      value: "city",
      align: "center",
      sortable: false,
      width: "25%",
    },
  ];

  isLoading = false;

  get userTool() {
    return _.find(
      mainStore.currentUserTools,
      { tool_id: 1 } || {
        allow_create: false,
        allow_read: false,
        allow_update: false,
        allow_delete: false,
      }
    );
  }

  get users() {
    return adminStore.users;
  }

  async confirmDelete(user: IUserProfile) {
    console.log(user);
    this.$swal({
      icon: "warning",
      title: "Tem certeza?",
      text: "O usuário não poderá ser recuperado",
      ...this.swalDefaults,
    }).then(async (result) => {
      if (result.isConfirmed) {
        await adminStore.deleteUser(user.id!);
      }
    });
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