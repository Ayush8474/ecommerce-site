<template>
    <div class = "cart-page">
        <div class = "columns is-multiline">
             <table class="table" v-if="cartTotalLength">
                  <thead>
                    <tr>
                      <th>Product Name</th>
                      <th>Price</th>
                      <th>Quantity</th>
                      <th>Subtotal</th>
                      <th>  </th>
                    </tr>

                  </thead>

                    <tbody>
                        <CartProductView v-for="item in cart.items" v-bind:key = "item.product.id" v-bind:itemProp="item">
                        </CartProductView>

                        <tr>
                        <td></td>
                        <td></td>
                        <td>No. of items: {{cartTotalLength}}</td>
                        <td><strong>Total: {{cartTotal}}</strong></td>
                        <td></td>
                        </tr>
                    </tbody>

             </table>
             <p v-else>Cart is empty. Start Shopping!</p>

        </div>
    </div>
</template>


<script>

import axios from 'axios'
import CartProductView from '../views/CartProductView.vue'

export default {
  name: 'CartView',
  data() {
    return {
        cart : {
            items : [],
        },
    }
  },
  components: {
    CartProductView,
  },
  mounted() {
    this.cart = this.$store.state.cart
  },
  computed: {
        cartTotalLength() {
            let totalLength = 0;
            for (let i = 0; i < this.cart.items.length; i++) {
                totalLength += this.cart.items[i].quantity
            }

            return totalLength
        },
        cartTotal() {
            let totalPrice = 0;
            for (let i = 0; i < this.cart.items.length; i++) {
                totalPrice += parseInt(this.cart.items[i].quantity) * parseInt(this.cart.items[i].product.price)
            }

            return totalPrice
        },
  },
  methods: {

  },
}
</script>
