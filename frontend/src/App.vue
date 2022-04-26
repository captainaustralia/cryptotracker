<template>
  <div id="nav">
    <div v-if="this.auth === 'true'">
      <router-link to="/">Home</router-link>
      <router-link to="/about">About</router-link>
    </div>
    <div v-if="this.auth !== 'true'">
      <router-link to="/login">Login |</router-link>
      <router-link to="/register">Register</router-link>
    </div>
    <button class="btn btn-primary" type="button" @click="logout">Logout</button>
  </div>
  <router-view/>
</template>

<script>
import router from "@/router";

export default {
  data() {
    return {
      auth: localStorage.getItem('auth'),
    }
  },
  methods: {
    logout() {
      localStorage.removeItem('access')
      localStorage.removeItem('refresh')
      localStorage.removeItem('auth')
      this.auth = ''
      this.user_id = ''
      router.push('/login')
    }
  }
}
</script>
<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #4276b9;
}

#nav {
  padding: 15px;
  text-align: right;
  width: 100%;
  background-color: black;
  border-bottom: solid 2px white;
}

#nav a {
  font-weight: bold;
  color: #ffffff;
}

#nav a.router-link-exact-active {
  color: rgba(220, 220, 220, 0.63);
}
</style>
