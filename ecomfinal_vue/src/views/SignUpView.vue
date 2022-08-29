<template>
    <div class = "signup-page">
        <div class="field">
          <p class="control has-icons-left has-icons-right">
            <input class="input" type="email" placeholder="Email">
            <span class="icon is-small is-left">
              <i class="fas fa-envelope"></i>
            </span>

          </p>
        </div>
        <div class="field">
          <p class="control has-icons-left">
            <input class="input" type="password" placeholder="Password">

          </p>
        </div>
    </div>
</template>


<script>

import axios from 'axios'

export default {
  name: 'SignUpView',
  data() {
    return {
        username : {},
        password : {},
        email : {},
    }
  },
  components: {

  },
  mounted() {

  },
  computed: {

  },
  methods: {

  },
}
</script>



<style lang="scss">
  @import '../../node_modules/bulma';
</style>