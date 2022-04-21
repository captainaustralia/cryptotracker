<template>
  <div class="container-fluid">
    <div>
      <h1>hello</h1>
      <h1>hello</h1>
      <h1>hello</h1>
    </div>
  </div>
  <coin-form @remove="removeCoin" v-bind:coins="coins"/>
  <add-coin @add="addCoin"/>
</template>

<script>
import axios from "axios";
import CoinForm from "@/components/CoinForm";
import AddCoin from "@/components/AddCoin";
import TradingView from "@/components/TradingView";

export default {
  name: 'Home',
  components: {TradingView, AddCoin, CoinForm},
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
      this.coins = response.data[0]['coins']
      this.portfolio = response.data[0]['name']
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
    },
    async addCoin(coin) {
      const response = await axios.post(`http://127.0.0.1:8000/api/addtoken/`, {
        name: coin.name,
        buy_price: coin.buy_price,
        coin_price: coin.coin_price,
        amount: coin.amount
      }, {
        headers: {
          Authorization: `Bearer ${localStorage.getItem('access')}`
        }
      })
      if (response.status === 201) {
        this.coins.push(coin)
      }
    }
  },
  mounted() {
    this.takePortfolio();
  }
}

</script>
