<template>
  <div style="text-align: center">
    <h2>Parent</h2>
    <input type="text" @change="onchange">
    <p>appData: {{appData}}</p>
    <p>childData: {{childData}}</p>
    <Child
      :appData='appData'
      :parentData='parentData'
      :childData='childData'
      @onChildChange='onChildChange'
    />
  </div>
</template>

<script>
import Child from '@/components/Child.vue'

export default {
  components: {
    Child,
  },
  props: {
    appData: String,
    parentData: String,
    childData: String,
  },
  methods: {
    onchange: function (event) {
      this.$emit('onParentChange',event.target.value)
    },
    onChildChange: function (text) {
      this.$emit('onChildChange', text)
    }
  }
}
</script>