<template>
  <div class="container">
    <h1>My First Youtube Project</h1>
    <SearchBar @input-change="onInputChange" />
    <VideoList :videos='videos' @select-video='onVideoSelect'/>
    <VideoDetail :video='selectedVideo'/>
  </div>
</template>

<script>
import axios from 'axios'

import SearchBar from '@/components/SearchBar'
import VideoList from '@/components/VideoList'
import VideoDetail from '@/components/VideoDetail'

const API_KEY = 'AIzaSyCsh655apyg5BX0yuWowxu0gZRrIeqc2_I'
const API_URL = 'https://www.googleapis.com/youtube/v3/search'


export default {
  name: 'App',
  components: {
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
      this.inputValue = inputText

      const params = {
        key: API_KEY,
        part: 'snippet',
        type: 'video',
        q: this.inputValue,
      }

      axios.get(API_URL, {
        params,
      })
      .then((res) => {
        this.videos = res.data.items
      })
      .catch((err) => {
        console.log(err)
      })
    },
    onVideoSelect: function (video) {
      this.selectedVideo = video
    }
  },
  watch: { // 변수이름과 같은 이름의 함수를 지정하면 그 값이 변할때마다 작동하게 된다. 말 그대로 감시자의 역할을 한다
    inputValue: function(value) { // 이 코드에서 value는 입력 받은 값을 의미
      console.log('watch',value)
    }
  },
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