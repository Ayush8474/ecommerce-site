<template>
    <div id = "wrapper">
        <nav class="navbar is-dark">
            <div class="navbar-brand">
                <router-link to="/" class="navbar-item"><strong>Home</strong></router-link>
                 <a class="navbar-burger" aria-label="menu" aria-expanded="false" data-target="navbar-menu">
                    <span aria-hidden="true"></span>
                    <span aria-hidden="true"></span>
                    <span aria-hidden="true"></span>
                 </a>
            </div>

            <div class = "navbar-menu" id = "navbar-menu">
                <div class ="navbar-start">
                    <div class="navbar-item">
                        <form method = "get" action = "/search">
                            <div class = "field has-addons">
                                <div class = "control">
                                    <input type = "text" class = "input"
                                    placeholder="Search for products" name ="query">
                                </div>

                                <div class="control">
                                    <button class = "button is-success">
                                        <span class = "searchButton">
                                            Go!
                                        </span>
                                    </button>
                                </div>
                            </div>
                        </form>
                    </div>
                </div>


                <div class = "navbar-end">
                    <router-link :to="category.get_absolute_url" class="navbar-item"
                     v-for="category in categories" :key = "category.id"
                    >{{category.name}}</router-link>

                    <div class = "navbar-item">
                        <div class = "buttons">
                            <router-link to="/login" class ="button is-light">Log In</router-link>
                            <router-link to="/cart" class ="button is-danger">
                                <span>Cart({{cartTotalLength}})</span>
                            </router-link>
                        </div>
                    </div>
                 </div>
             </div>
        </nav>
    </div>
  <section class = "section">
    <router-view></router-view>
  </section>

  <footer class = "footer">
    <p class="has-text-centered">Open Source project by Ayush, 2022</p>
   </footer>
</template>

<script>

import axios from 'axios'
export default {
    data() {
        return {
            cart: {
                items :[],
            },
            categories:[],

        }
    },
    mounted() {
        this.cart = this.$store.state.cart
        this.getCategories()
    },
    beforeCreate() {
        this.$store.commit('initialiseStore')
    },
    computed: {
        cartTotalLength() {
            let totalLength = 0;
            for (let i = 0; i < this.cart.items.length; i++) {
                totalLength += this.cart.items[i].quantity
            }

            return totalLength
        },
    },
    methods:{
        getCategories() {
            axios.get('/api/categories/')
            .then(response=> {
                this.categories = response.data;
                console.log("categories fetched.");
            }).catch (error => {
                console.log(error)
             })
        },
    },
}
</script>

<style lang="scss">
@import '../node_modules/bulma';
</style>
