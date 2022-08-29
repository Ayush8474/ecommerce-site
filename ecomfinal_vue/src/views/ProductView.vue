<template>
    <div class = "product-page">
        <div class="columns is-mobile">
             <div class="column is-three-fifths is-offset-one-fifteenth">
                <div class="box">
                    <figure class="image is-200x200">
                        <img :src = "product.get_image">
                    </figure>
                </div>
             </div>

             <div class="column">
                <div class="box">
                  <p class="title is-5">{{product.name}}</p>
                  <p class="subtitle">{{product.description}}</p>
                </div>
            </div>
        </div>

        Select Quantity
        <div class="field has-addons">
          <div class="control">
           <input class="input is-medium" type="number" placeholder="Select Quantity" v-model="quantity">
          </div>
          <div class="control">
            <a class="button is-info" @click = "addToCart">
              Submit
            </a>
          </div>
        </div>
    </div>


</template>


<script>

import axios from 'axios'

export default {
  name: 'ProductView',
  data() {
    return {
        product:{},
        quantity: 0,
    }
  },
  components: {
  },
  mounted() {
    this.getProduct()
  },

  methods: {
    getProduct() {
        const category_slug = String(this.$route.params.category_slug)
        const product_slug = String(this.$route.params.product_slug)
        console.log(category_slug)
        console.log(product_slug)
        axios.get('/api/products/'+category_slug+'/'+product_slug).then(
            response=>{
                this.product= response.data
                document.title = this.product.name + " | Fashion Sultana"
            }
        ).catch( error => {console.log(error)})
    },
    addToCart() {
        if (!(isNaN(this.quantity) || this.quantity < 1)) {
            console.log("quantity is: "+this.quantity)
            const item = {
                product: this.product,
                quantity: this.quantity,
            }
            this.$store.commit('addToCart', item)

        }
    },
  }
}
</script>
