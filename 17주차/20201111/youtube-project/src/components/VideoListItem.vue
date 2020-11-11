<template>
  <li @click="selectVideo">
    <img :src="youtubeImageSrc" alt="">
    <!-- <span v-html="video.snippet.title"></span> -->
    {{video.snippet.title | stringUnescape}}
  </li>
</template>

<script>
import _ from 'lodash'

export default {
  name: 'VideoListItem', 
  props: {
    video: Object,
  },
  methods: {
    selectVideo: function () {
      this.$emit('select-video', this.video)
    }
  },
  computed: {
    youtubeImageSrc: function () {
      return this.video.snippet.thumbnails.default.url
    }
  },
  filters: {
    stringUnescape: function (rawText) {
      console.log(rawText)
      return _.unescape(rawText)
    }
  }
}
</script>