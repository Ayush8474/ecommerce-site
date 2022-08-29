<template>
    <div class = "category-page">
        <div class="columns is-multiline">
            <div class ="column is-12">
                <h2 class = "is-size-2">{{category}}</h2>
            </div>

            <div class="column is-3" v-for="product in products_of_this_category"
            v-bind:key = "product.id">
                <div class ="box">
                    <figure class="image is-4by5">
                        <img :src="product.get_thumbnail">
                    </figure>
                    <h3 class = "is-size-4">{{product.name}}</h3>
                    <p class = "is-size-6 has-text-grey">Rs.{{product.price}}</p>
                    <router-link :to="product.get_absolute_url">
                        <button class="button is-rounded">View Details</button>
                    </router-link>
                 </div>
            </div>
        </div>
    </div>
</template>


<script>

import axios from 'axios'

export default {
  name: 'CategoryView',
  data() {
    return {
        products_of_this_category: [],
        category:'',
    }
  },
  components: {
  },
  mounted() {
    this.getProducts()
  },
  methods: {
    async getProducts() {
        const category_slug = String(this.$route.params.category_slug)
        console.log(category_slug)
        await axios.get('/api/products/'+category_slug).then(
            response=>{
                this.products_of_this_category = response.data["products"]
                this.category = response.data["name"]
                document.title = this.category + " | Fashion Sultana"
            }
        ).catch( error => {console.log(error)})
    },
  },
}
</script>