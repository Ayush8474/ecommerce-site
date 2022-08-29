<template>
  <div class="home">
    <section class="hero is-medium is-link">
      <div class="hero-body has-text-centered">
        <p class="title">
          Fashion Sultana
        </p>
        <p class="subtitle">
          Your one-stop fashion solution
        </p>
      </div>
    </section>

    <p class="mb-4">

    </p>

    <div class = "columns is-multiline">
         <div class="column is-12">
            <h2 class = "is-size-2 has-text-centered">Latest products</h2>
         </div>
         <div class="column is-3" v-for="product in latestProducts"
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
  name: 'HomeView',
  data() {
    return {
        latestProducts: [],
    }
  },
  components: {
  },
  mounted() {
    this.getLatestProducts()
  },

  methods: {
    getLatestProducts() {
        axios.get('/api/latest/')
        .then(response=> {
            this.latestProducts = response.data;
            console.log("latest products fetched.");
            document.title = "Home | Fashion Sultana";
        }).catch (error => {
            console.log(error)

         })
    }
  }
}
</script>
