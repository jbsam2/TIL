<template>
  <div v-if='video'>
    <iframe :src="videoURI" frameborder="0"></iframe>
    {{video.snippet.title | stringUnescape}}
  </div>
</template>

<script>
import _ from 'lodash'

export default {
  name: 'VideoDetail', 
  props: {
    video: [Object, String],
  },
  computed: {
    videoURI: function () {
      const videoId = this.video.id.videoId
      return `https://www.youtube.com/embed/${videoId}`
    }
  },
  filters: {
    stringUnescape: function (rawText) {
      return _.unescape(rawText)
    }
  }
}
</script>