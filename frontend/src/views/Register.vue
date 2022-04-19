<template>
  <section class="vh-80 gradient-custom">
    <div class="container py-5 h-100">
      <div class="row d-flex justify-content-center align-items-center h-100">
        <div class="col-12 col-md-8 col-lg-6 col-xl-5">
          <div class="card bg-dark text-white" style="border-radius: 1rem;">
            <div class="card-body p-5 text-center">
              <div class="mb-md-5 mt-md-4 pb-5">
                <h2 class="fw-bold mb-2 text-uppercase">Register</h2>
                <p class="text-white-50 mb-5">Please enter your email,username and password</p>
                <div class="form-outline form-white mb-4">
                  <input v-model="email" type="email" id="typeEmailX" class="form-control form-control-lg"/>
                  <label class="form-label" for="typeEmailX">Email</label>
                </div>
                <div class="form-outline form-white mb-4">
                  <input v-model="username" type="text" id="typeUsernameX" class="form-control form-control-lg"/>
                  <label class="form-label" for="typeEmailX">Username</label>
                </div>
                <div class="form-outline form-white mb-4">
                  <input v-model="password" type="password" id="typePasswordX" class="form-control form-control-lg"/>
                  <label class="form-label" for="typePasswordX">Password</label>
                </div>
                <button @click="register" class="btn btn-outline-light btn-lg px-5" type="submit">Register</button>
              </div>
              <div>
                <p class="mb-0">Already have account? <a href="" class="text-white-50 fw-bold"> <router-link to="/login">Login</router-link></a>
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
  name: "Register",
  data() {
    return {
      email: '',
      username: '',
      password: '',
    }
  },
  methods: {
    async register() {
      try {
        const response = await axios.post('http://127.0.0.1:8000/api/register/', {
          email: this.email,
          username: this.username,
          password: this.password
        })
        await router.push('/login')
      } catch (e) {
        alert('Something wrong')
      }

    }
  }
}
</script>

<style scoped>

</style>