<template>
  <div>
    <ul>
      <VideoListItem
        v-for='(video, idx) in videos' :key='idx'
        :video='video'
        @select-video='onVideoSelect'
      />
    </ul>
  </div>
</template>

<script>
import VideoListItem from '@/components/VideoListItem'

export default {
  name: 'VideoList', 
  components: {
    VideoListItem,
  },
  props: {
    videos: Array,
  },
  methods: {
    onVideoSelect: function (video) {
      this.$emit('select-video',video)
    }
  }
}
</script>