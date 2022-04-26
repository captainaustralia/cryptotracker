<template>
  <div class="main_container">
    <div class="avatar_container">
      <img class="avatar_log" src="../assets/123.jpg">
    </div>
    <div class="info_container">
      <div class="info">
        <div class="text">
          <p class="text_info">E-mail: {{ user_info.email }}</p>
          <p class="text_info">Username : {{ user_info.username }}</p>
          <p class="text_info">Portfolio : {{ portfolio_names.length }}</p>
          <p class="text_info">Coins : 100</p>
          <p class="text_info">Top 5 coins : </p>
          <p class="text_info">Total cash : </p>
        </div>
      </div>
    </div>
  </div>
  <select v-model="current" @change="currentPortfolioCoin(current)">
    <option v-for="name in portfolio_names">{{ name }}</option>
  </select>
  <portfolio-create-form @addPortfolio="createNewPortfolio"/>
  <coin-form @remove="removeCoin" v-bind:coins="coins"/>
  <add-coin @add="addCoin"/>
</template>

<script>
import axios from "axios";
import CoinForm from "@/components/CoinForm";
import AddCoin from "@/components/AddCoin";
import TradingView from "@/components/TradingView";
import PortfolioCreateForm from "../components/PortfolioCreateForm";

export default {
  name: 'Home',
  components: {PortfolioCreateForm, TradingView, AddCoin, CoinForm},
  data() {
    return {
      portfolio: '',
      coins: Object,
      data: '',
      user_info: '',
      portfolio_names: [],
      current: localStorage.getItem('selected_portfolio')
    }
  },
  methods: {
    async takePortfolio() {
      const response = (await axios.get('http://127.0.0.1:8000/api/portfolio/', {
        headers: {
          Authorization: `Bearer ${localStorage.getItem('access')}`
        }
      }))
      for (let i in response.data) {
        this.portfolio_names.push(response.data[i]['name'])
      }
      this.data = response.data
      this.coins = response.data.filter((elements) => elements.name === this.current)[0]['coins']
      this.portfolio = response.data[0]['name']
      return this.data
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
        amount: coin.amount,
        portfolio: this.current
      }, {
        headers: {
          Authorization: `Bearer ${localStorage.getItem('access')}`
        }
      })
      if (response.status === 201) {
        this.coins.push(this.coin)
      }
    },

    async takeInfo() {
      const response = await axios.get('http://127.0.0.1:8000/api/me/', {
        headers: {
          Authorization: `Bearer ${localStorage.getItem('access')}`
        }
      })
      if (response.status === 200) {
        this.user_info = response.data
      }
    },

    currentPortfolioCoin(name) {
      this.coins = this.data.filter((elements) => elements.name === name)[0]['coins']
      localStorage.setItem('selected_portfolio', this.current)
    },

    async createNewPortfolio(name) {
      const response = await axios.post('http://127.0.0.1:8000/api/addportfolio/', {name:name}, {
        headers: {
          Authorization: `Bearer ${localStorage.getItem('access')}`
        }
      })
      if (response.status === 201){
        this.portfolio_names.push(name)
      }
    }
  },

  mounted() {
    this.takePortfolio();
    this.takeInfo();
  }
}

</script>

<style>
.main_container {
  width: 100%;
  height: 50vh;
  display: flex;
  background-color: #343a40 !important;
}

.avatar_container {
  display: flex;
  width: 30%;
  height: 55vh;
  justify-content: center;
  align-items: center;
  margin-left: 3%;
}

.info_container {
  width: 70%;
  height: 50vh;
}

img.avatar_log {
  width: 300px;
  height: 300px;
  background-color: black;
  border-radius: 50%;
  border: solid 2px white;
}

.info {
  margin-top: 5%;
  height: 70%;
  width: 70%;
  background-color: rgba(255, 255, 255, 0.16);
  border-radius: 2%;
  border: solid 2px white;
}

.text {
  margin-top: 6%;
  height: 100%;
  width: 100%;
}

.text_info {
  margin-left: 5%;
  color: white;
  font-size: 20px;
}

</style>