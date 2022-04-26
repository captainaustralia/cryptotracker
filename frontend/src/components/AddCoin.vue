<template>
  <div>
    <form>
      <input v-model="coin.name" placeholder="Token name">
      <input v-model="coin.buy_price" placeholder="need delete">
      <input v-model="coin.coin_price" placeholder="Token price">
      <input v-model="coin.amount" placeholder="Amount">
      <button @click="addCoin"  class="btn">Add</button>
    </form>
  </div>
</template>

<script>
export default {
  name: "AddCoin",
  data() {
    return {
      coin: {
        name: '',
        buy_price: 0,
        coin_price: 0,
        amount: 0
      }
    }
  },
  methods: {
    addCoin() {
      this.$emit('add', this.coin)
    }
  }
}
</script>

<style scoped>

</style>