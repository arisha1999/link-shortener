<template>
  <div id="urlInput">
    <v-text-field clearable label="URL" variant="outlined" type="text" id="full-url" :value="fullUrl" @input="updateUrl"></v-text-field>
  </div>
</template>

<script>
export default {
  props: {
    url: {
      type: String,
      default: ''
    }
  },
  computed: {
    fullUrl: {
      get() {
        return this.url;
      },
      set(value) {
        this.$emit('update:url', value);
      }
    }
  },
  methods: {
    updateUrl(event) {
      this.fullUrl = event.target.value;
    }
  }
}
</script>


<style>
  #urlInput{
    margin-bottom: 10px;
  }
</style>