<template>
  <TemplateCard :title="`Olá, ${currentUser.full_name}.`">
    <template>
      <div class="ma-10 d-flex flex-column align-center">
        <a
          target="_blank"
          href="https://v2.vuejs.org/"
          rel="noopener noreferrer"
        >
          <v-img contain src="@/assets/vue-logo.png" width="500" />
        </a>
        <a
          href="https://www.python.org/"
          target="_blank"
          rel="noopener noreferrer"
        >
          <v-img contain src="@/assets/python-logo.png" width="500" />
        </a>
      </div>
    </template>
  </TemplateCard>
</template>

<script lang="ts">
import Component from "vue-class-component";
import Vue from "vue";
import { mainStore } from "@/store";
import TemplateCard from "@/components/TemplateCard.vue";

@Component({
  components: {
    TemplateCard,
  },
})
export default class Home extends Vue {
  get currentUser() {
    return mainStore.userProfile!;
  }
  mounted() {}
}
</script>

<style>
</style>