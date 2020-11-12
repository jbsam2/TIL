<template>
  <div id="app">
    <h2>Cat Image</h2>
    <p><img :src="caturl" alt="" width="50%"></p>
    <button @click="geturl">Get Cat</button>
  </div>
</template>

<script>
import axios from 'axios'

const API_URL = 'https://api.thecatapi.com/v1/images/search'

export default {
  name: 'App',
  data(){
    return {
      caturl: '',
    }
  },
  methods: {
    geturl(){
      axios.get(API_URL)
      .then((res)=>{
        this.caturl = res.data[0].url
      })
    }
  },
  created() {
    this.geturl()
    console.log('created!',this.caturl)
  },
  mounted() {
    console.log('mounted!')
  },
  updated() {
    console.log('updated!',this.caturl)
  },
}
</script>