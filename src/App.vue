<template>
  <div id="app">
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  created: function(){
    document.title = this.$route.meta.title || this.$route.meta.pathName
  },
  watch:{
    $route(){
      document.title = this.$route.meta.title || this.$route.meta.pathName
    }
  },
  methods: {
  }
}
</script>

<style>
</style>
