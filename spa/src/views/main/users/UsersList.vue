<template>
  <TemplateCard title="Usuários">
    {{ users }}
  </TemplateCard>
</template>

<script lang="ts">
import Component from "vue-class-component";
import Vue from "vue";
import TemplateCard from "@/components/TemplateCard.vue";
import { adminStore } from "@/store";

@Component({
  components: {
    TemplateCard,
  },
})
export default class UsersList extends Vue {
  get users() {
    return adminStore.users;
  }

  async mounted() {
    await adminStore.getUsers();
  }
}
</script>

<style>
</style>