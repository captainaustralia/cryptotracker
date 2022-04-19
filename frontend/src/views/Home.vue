<template>
  <div class="container-fluid">
    <div class="profile">
      <div class="row">
        <div class="col-2 h-50">
          <h4>@username</h4>
        </div>
      </div>
      <div class="row">
        <div class="col-2 h-50">
          <h4>@email</h4>
        </div>
      </div>
      <div class="row justify-content-md-center">
        <div class="col text-center" style="margin:20px">
          <p>Portfolio Name :<strong>{{ portfolio }}</strong></p>
        </div>
      </div>
      <div class="info">

      </div>
    </div>
    <div class="table">
      <table class="table table-light">
        <thead>
        <tr>
          <th scope="col"></th>
          <th scope="col">Token</th>
          <th scope="col">Buy price</th>
          <th scope="col">Coin price</th>
          <th scope="col">Amount</th>
          <th scope="col">% up/down</th>
          <th scope="col">Graph</th>
        </tr>
        </thead>
        <tbody>
        <tr v-for="(coin,ind) in coins">
          <th scope="row">{{ ind + 1 }}</th>
          <td>{{ coin['name'] }}</td>
          <td>{{ coin['buy_price'] }} $</td>
          <td>{{ coin['coin_price'] }} $</td>
          <td>{{ coin['amount'] }}</td>
          <td></td>
        </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: 'Home',
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

    async fetchPrice(name) {
      setInterval(async () => {
        const price = await fetch(`https://min-api.cryptocompare.com/data/price?fsym=${name}&tsyms=USD&api_key=1188a92804a7191cda39795614628122e24350f53e3defb630dfe1ba0162a0ff`);
        const data = await price.json();
        console.log(data);
      }, 5000);
    },
    async addToken(name) {
      setInterval(async () => {
        const price = await axios.post('http://127.0.0.1:8000/api/addtoken/');
        const data = await price.json();
        console.log(data);
      }, 5000);
    },
    async test(){
      const rofl = await axios.post('http://127.0.0.1:8000/api/token/verify/')
    }

  },
  mounted() {
    this.takePortfolio();
    this.fetchPrice('BTC')
  }
}
</script>
