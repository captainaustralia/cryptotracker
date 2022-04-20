<template>
  <div class="container-fluid">
    <div>
        <h1>hello</h1>
        <h1>hello</h1>
        <h1>hello</h1>
    </div>

  </div>
  <coin-form @remove="removeCoin" v-bind:coins="coins"/>
</template>

<script>
import axios from "axios";
import CoinForm from "@/components/CoinForm";

export default {
  name: 'Home',
  components: {CoinForm},
  data() {
    return {
      portfolio: '',
      coins: [],
    }
  },
  methods: {
    async takePortfolio() {
      const response = (await axios.get('http://127.0.0.1:8000/api/portfolio/', {
        headers: {
          Authorization: `Bearer ${localStorage.getItem('access')}`
        }
      }))
      console.log(response.data)
      this.coins = response.data[0]['coins']
      this.portfolio = response.data[0]['name']
      console.log(this.coins)
    },
    async removeCoin(coin) {
      const response = await axios.delete(`http://127.0.0.1:8000/api/deletetoken/${coin.id}`, {
        headers: {
          Authorization: `Bearer ${localStorage.getItem('access')}`
        }
      })
      if (response.status === 202) {
        this.coins = this.coins.filter(c => c.id !== coin.id)
      }
    }
  },
  mounted() {
    this.takePortfolio();
  }
}

</script>
