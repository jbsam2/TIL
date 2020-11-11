<template>
  <div>
    <h2>로또</h2>
    <button @click='lotto'>Get Lucky Numbers</button>
    <p>{{luckyNumber}}</p>
  </div>
</template>

<script>
import _ from 'lodash'
export default {
  name: 'TheLotto',
  data: function () {
    return {
      luckyNumber: '',
    }
  },
  methods: {
    lotto: function(){
      const result = _.sampleSize(_.range(1, 46), 6)
      this.luckyNumber = _.sortBy(result)
    }
  }
}
</script>

<style>

</style>