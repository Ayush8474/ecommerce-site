import { createStore } from 'vuex'

export default createStore({
  state: {
    cart : {
    items: [],
    },
    isAuthenticated : false,
    token : '',
  },
  getters: {
  },
  mutations: {
    initialiseStore(state) {
        if (localStorage.getItem('cart')) {
            state.cart = JSON.parse(localStorage.getItem('cart'))
        }
        else {
            localStorage.setItem('cart', JSON.stringify(state.cart))
        }
    },
    addToCart(state, item) {
        const exists = state.cart.items.filter(
             i => i.product.id === item.product.id
        )
        console.log(exists.length)

        if (exists.length) {
            exists[0].quantity = parseInt(exists[0].quantity) + parseInt(item.quantity)
        }
        else {
            state.cart.items.push(item);
        }

        localStorage.setItem('cart', JSON.stringify(state.cart))
    },
    removeFromCart(state, item) {
        const index = state.cart.items.indexOf(item);
        if (index > -1) {
           state.cart.items.splice(index, 1);
           localStorage.setItem('cart', JSON.stringify(state.cart))
        }

    },


  },
  actions: {
  },
  modules: {
  }
})
