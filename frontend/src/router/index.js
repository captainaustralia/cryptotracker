import {createRouter, createWebHistory} from 'vue-router'
import Home from '../views/Home.vue'
import Login from "@/views/Login";
import Register from "@/views/Register";
import axios from "axios";

const routes = [
    {
        path: '/',
        name: 'Home',
        component: Home
    },
    {
        path: '/about',
        name: 'About',
        component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
    },
    {
        path: '/login',
        name: 'Login',
        component: Login
    },
    {
        path: '/register',
        name: 'Register',
        component: Register
    },
]


const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
})


router.beforeEach((to, from, next) => {
    const publicPages = ['/login', '/register'];
    if (!publicPages.includes(to.path)) {
        if (localStorage.getItem('access') !== null && localStorage.getItem('refresh') !== null) {
            verify().then(next()).catch(err => {
                if (err.response.status === 401) {
                    refresh().then(next)
                }
            })
        } else {
            localStorage.setItem('auth', false)
            next('/login')
        }
    } else {
        next()
    }
})
export default router

async function verify() {
    return await axios.post('http://127.0.0.1:8000/api/token/verify/', {token: localStorage.getItem('access')})
}

async function refresh() {
    const res = await axios.post('http://127.0.0.1:8000/api/token/refresh/', {refresh: localStorage.getItem('refresh')})
    localStorage.setItem('access', res.data['access'])
}