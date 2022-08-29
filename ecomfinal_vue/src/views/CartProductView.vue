<template>
    <tr>
        <td><router-link :to = "item.product.get_absolute_url">{{item.product.name}}</router-link></td>
        <td>Rs. {{item.product.price}}</td>
        <td>{{item.quantity}}</td>
        <td>Rs. {{getSubTotal}}.00</td>
        <td>
            <div class ="button is-danger" @click="deleteItem(item)">
                <span>Remove</span>
            </div>
        </td>
    </tr>
</template>


<script>

export default {
  name: 'CartProductView',
  data() {
    return {
        item : this.itemProp
    }
  },
  props : {
        itemProp:Object,
  },
  mounted() {
  },
  computed: {
    getSubTotal() {
        let price = parseInt(this.item.product.price)
        let qty = parseInt(this.item.quantity)
        //console.log("price:"+price+", qty:"+qty)
        return price*qty
    }
  },
  methods: {
        deleteItem(item) {
            this.$store.commit("removeFromCart", item)
            this.item = {}
        },
  },
}
</script>
