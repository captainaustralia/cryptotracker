<template>
  <form>
    <input v-model="name" placeholder="New portfolio">
    <button @click="createPortfolio" class="btn btn-success">Create new portfolio</button>
  </form>
</template>

<script>

export default {
  name: "PortfolioCreateForm",
  data() {
    return {
      name: ''
    }
  },
  methods: {
    createPortfolio() {
      this.$emit('addPortfolio', this.name)
    }
  }
}
</script>

<style scoped>

</style>