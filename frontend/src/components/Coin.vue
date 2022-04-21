<template>
  <tr>
    <th scope="row">
      <button class="btn btn-danger" @click="$emit('remove',coin)"> - </button>
    </th>
    <td>{{ coins_data['name'] }}</td>
    <td>{{ coins_data['coin_price'] }} $</td>
    <td>{{ coins_data['amount'] }}</td>
    <td>{{ current_price }} $</td>
    <td>{{ percent }} % ({{(current_price * coins_data['amount'] - coins_data['coin_price'] * coins_data['amount'] ).toFixed(2)}} $)</td>
    <td><img src="https://s3.coinmarketcap.com/generated/sparklines/web/7d/2781/825.svg" alt="tether-7d-price-graph"
             class="h7vnx2-0 bCltOL isUp" loading="lazy">
    </td>
  </tr>
</template>

<script>
export default {
  inheritAttrs: false,
  name: "Coin",
  props: {
    coins_data: {
      type: Object,
      default() {
        return {}
      }
    },
  },
  data() {
    return {
      current_price: 0,
      percent: 0
    }
  },

  methods: {
    async getPrice(name) {
      setInterval(async () => {
        const price = await fetch(`https://min-api.cryptocompare.com/data/price?fsym=${name}&tsyms=USD&api_key=1188a92804a7191cda39795614628122e24350f53e3defb630dfe1ba0162a0ff`);
        const data = await price.json();
        this.current_price = data['USD']
      }, 1000);
    },
    async countPercent(){
      setInterval(async () =>{
        if (this.coins_data['coin_price'] < this.current_price){
          this.percent =  ((this.current_price * 100) / this.coins_data['coin_price'] - 100).toFixed(2)
        } else{
          this.percent =  - (100 - (this.current_price * 100) / this.coins_data['coin_price']).toFixed(2)
        }
      }, 1000)
    },
    async deleteToken(id){
      this.$emit('delete',)
    }
  },
  mounted() {
    this.getPrice(this.coins_data.name)
    this.countPercent()
  }
}
</script>

<style scoped>

</style>