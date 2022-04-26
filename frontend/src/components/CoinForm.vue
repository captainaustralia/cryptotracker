<template>
  <div class="table">
    <table class="table table-dark">
      <thead class="text-center">
      <tr>
        <th scope="col"></th>
        <th scope="col">Token</th>
        <th scope="col">Coin price</th>
        <th scope="col">Amount</th>
        <th scope="col">Current token Price</th>
        <th scope="col">% up/down</th>
        <th scope="col">Graph</th>
      </tr>
      </thead>
      <tbody class="text-center">
      <coin
          v-for="coin in coins"
          :key="coin.id"
          :coins_data="coin"
          v-bind="coin"
          @remove="$emit('remove',coin)"
      />
      </tbody>
    </table>
  </div>
</template>

<script>
import Coin from "@/components/Coin";

export default {
  name: "CoinForm",
  components: {Coin},
  props: {
    coins: {
      type: Array,
      required: true
    },
  },
}
</script>

<style scoped>
</style>