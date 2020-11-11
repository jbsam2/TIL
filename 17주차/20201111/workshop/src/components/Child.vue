<template>
  <div style="text-align: center">
    <h2>Child</h2>
    <input type="text" @change="onchange">
    <p>appData: {{appData}}</p>
    <p>parentData: {{parentData}}</p>
  </div>
</template>

<script>
export default {
  props: {
    appData: String,
    parentData: String,
    childData: String,
  },
  methods: {
    onchange: function (event) {
      this.$emit('onChildChange',event.target.value)
    }    
  }
}
</script>