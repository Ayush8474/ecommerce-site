<template>
  <div class = "search-page">
    <div class = "columns is-multiline">
         <div class="column is-12">
            <h2 class = "is-size-2 has-text-centered">Search Results for "{{query}}"</h2>
         </div>
         <div class="column is-3" v-for="product in products"
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
  name: 'SearchView',
  data() {
    return {
        products: [],
        query : '',
    }
  },
  components: {
  },
  mounted() {
    this.getProducts()
  },

  methods: {
    getProducts() {
        let urlParams = new URLSearchParams(window.location.search);
        const query = urlParams.get('query');
        this.query = query
        console.log("queery is:"+query)
        axios.get('/api/search/'+query)
        .then(response=> {
            this.products = response.data;
            console.log("Search products fetched.");
            document.title = "Search Results | Fashion Sultana";
        }).catch (error => {
            console.log(error)
         })
    }
  }
}
</script>
