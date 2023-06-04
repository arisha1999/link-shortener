<template>
  <div class="shortUrl_field">
    <label for="short-url">Shortened URL:</label>
    <a :href="shortUrl" target="_blank" @click.prevent="openShortUrl">
      <p>{{ shortUrl }}</p>
    </a>
    <v-btn @click="copyShortUrl">Copy</v-btn>
  </div>
</template>

<script>
import axios from 'axios';
// import router from "../../router"
export default {
  props: {
    shortUrl: {
      type: String,
      default: ''
    }
  },
  methods: {
    openShortUrl() {
    axios.get(`http://localhost:5000/getredirecturl?short_url=${this.shortUrl}`)
        .then(response => {
          console.log(response.data);
          window.location.href = response.data;
        })
        .catch(error => {
          console.log(error);
          // router.push('/404');
        });
    },
    copyShortUrl() {
      const el = document.createElement('textarea');
      el.value = this.shortUrl;
      document.body.appendChild(el);
      el.select();
      document.execCommand('copy');
      document.body.removeChild(el);
    }
  }
}
</script>

<style>
  .shortUrl_field{
    display: flex;
    align-items: baseline;
    gap: 12px;
    margin-bottom: 20px;
  }
</style>