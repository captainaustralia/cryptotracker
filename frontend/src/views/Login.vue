<template>
  <section class="vh-70 gradient-custom">
    <div class="container py-5 h-100">
      <div class="row d-flex justify-content-center align-items-center h-100">
        <div class="col-12 col-md-8 col-lg-6 col-xl-5">
          <div class="card bg-dark text-white" style="border-radius: 1rem;">
            <div class="card-body p-5 text-center">
              <div class="mb-md-5 mt-md-4 pb-5">
                <h2 class="fw-bold mb-2 text-uppercase">Login</h2>
                <p class="text-white-50 mb-5">Please enter your email and password</p>
                <div class="form-outline form-white mb-4">
                  <input v-model="email" type="email" id="typeEmailX" class="form-control form-control-lg"/>
                  <label class="form-label" for="typeEmailX">Email</label>
                </div>
                <div class="form-outline form-white mb-4">
                  <input v-model="password" type="password" id="typePasswordX" class="form-control form-control-lg"/>
                  <label class="form-label" for="typePasswordX">Password</label>
                </div>
                <button @click="defaultLogin" class="btn btn-outline-light btn-lg px-5" type="submit">Log in</button>
              </div>
              <div>
                <p class="mb-0">Don't have an account yet? <a href="" class="text-white-50 fw-bold">
                  <router-link to="/register">Sign up</router-link>
                </a>
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import axios from "axios";
import router from "@/router";

export default {
  name: "Login",
  data() {
    return {
      email: '',
      password: '',
    }
  },
  methods: {
    async specLogin() {
      try {
        const response = (await axios.post('http://127.0.0.1:8000/api/spec_auth/', {
              email: this.email,
              password: this.password
            },
            {
              withCredentials: true,
            }))
        await router.push('/')
        console.log(response.data)
      } catch (e) {
        console.log(e)
      }
    },
    async defaultLogin() {
      try {
        const response = await axios.post('http://127.0.0.1:8000/api/token/', {
          email: this.email,
          password: this.password
        })
        const access = response.data['access']
        const refresh = response.data['refresh']
        localStorage.setItem('access', access)
        localStorage.setItem('refresh', refresh)
        localStorage.setItem('auth', true)
        await router.push('/')
      } catch (e) {
        alert('Wrong email/password')
      }
    }
  }
}
</script>

<style scoped>

</style>