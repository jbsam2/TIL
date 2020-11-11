<template>
  <div class="container">
    <h1>My First Youtube Project</h1>
    <!-- 3.보여준다. -->
    <SearchBar @input-change="onInputChange" />
    <VideoDetail :video='selectedVideo'/>
    <VideoList :videos='videos' @select-video='onVideoSelect'/>
  </div>
</template>

<script>
import axios from 'axios'

//1. 불러온다.
import SearchBar from '@/components/SearchBar'
import VideoList from '@/components/VideoList'
import VideoDetail from '@/components/VideoDetail'

const API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY
const API_URL = 'https://www.googleapis.com/youtube/v3/search'


export default {
  name: 'App',
  components: {
    // ES6 Object 축약 문법
    // SearchBar: SearchBar, 
    //2. 등록한다.
    SearchBar,
    VideoList,
    VideoDetail,
  },
  data: function () {
    return {
      inputValue: '',
      selectedVideo: '',
      videos: [],
    }
  },
  methods: {
    onInputChange: function (inputText) {
      console.log('데이터가 SearchBar로부터 올라왔다!!!!')
      console.log(inputText)

      //1. 자식 컴포넌트(SearchBar.vue)로부터 올라온 데이터 inputValue라는 App.vue 컴포넌트 데이터에 넣는다.
      this.inputValue = inputText

      //2. Youtube API로 요청을 위한 준비를 한다.
      const params = {
        key: API_KEY,
        part: 'snippet',
        type: 'video',
        q: this.inputValue,
      }

      //3. Youtube로 axios를 활용해 요청을 보낸다.
      axios.get(API_URL, {
        params,
      })
      .then((res) => {
        console.log(res)
        console.log(res.data.items)
      
        //4. Youtube로부터 응답 받은 영상 목록(배열)을 배열에 넣는다.
        this.videos = res.data.items
      })
      .catch((err) => {
        console.log(err)
      })
    },
    onVideoSelect: function (video) {
      this.selectedVideo = video
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
