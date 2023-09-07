<script lang="ts">
import Vue from "vue";
import Component from "vue-class-component";

@Component
export default class Mixins extends Vue {
  isValid = false;

  onSubmit() {}
}
</script>

<style scoped>
.container {
  background-color: var(--v-light);
  position: relative;
  height: 100vh;
}
</style>