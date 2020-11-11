<template>
  <div style="text-align: center">
    <h2>App</h2>
    <input type="text" v-model="appData">
    <p>parentData: {{parentData}}</p>
    <p>childData: {{childData}}</p>
    <Parent 
      :appData='appData'
      :parentData='parentData'
      :childData='childData'
      @onParentChange='onParentChange'
      @onChildChange='onChildChange'
    />
  </div>
</template>

<script>
import Parent from '@/components/Parent.vue'

export default {
  components: {
    Parent,
  },
  data: function () {
    return {
      appData: '',
      parentData: '',
      childData: '',
    }
  },
  methods: {
    onParentChange: function (parentData) {
      this.parentData = parentData
    },
    onChildChange: function (childData) {
      this.childData = childData
    }
  }
}
</script>