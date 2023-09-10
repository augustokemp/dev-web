<template>
  <TemplateCard title="Usuários"> aaa </TemplateCard>
</template>

<script lang="ts">
import Component from "vue-class-component";
import Vue from "vue";
import TemplateCard from "@/components/TemplateCard.vue";

@Component({
  components: {
    TemplateCard,
  },
})
export default class UsersList extends Vue {}
</script>

<style>
</style>