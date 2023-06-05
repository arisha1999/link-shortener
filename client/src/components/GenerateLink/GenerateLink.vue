<template>
  <div>
    <div class="firstUrl_input">
      <InputField :url="url" @update:url="updateUrl" />
      <v-btn variant="outlined" @click="generateShortUrl">
        Generate ShortURL
      </v-btn>
    </div>
    <ErrorAlert v-if="errorMessage" :error-message="errorMessage" />
    <div class="shortUrl_result">
      <div class="shortUrl_link">
        <ShortUrlField :shortUrl="shortUrl"/>
        <v-progress-circular v-if="showProgressBar" color="dark-blue" indeterminate :size="48"></v-progress-circular>
      </div>
      <img v-if="screenshot" :src="getImageUrl(screenshot)" alt="Screenshot"/>
    </div>
  </div>
</template>

<script>
import InputField from '@/components/InputField/InputField.vue';
import ShortUrlField from '@/components/ShortUrlField/ShortUrlField.vue'
import ErrorAlert from '../ErrorAlert/ErrorAlert.vue';
import axios from "axios"
export default {
  data() {
    return {
      url: '',
      errorMessage: '',
      shortUrl: '',
      screenshot: null,
      showProgressBar: false
    }
  },
  methods: {
    updateUrl(value) {
      this.url = value;
      this.errorMessage = '';
      this.shortUrl = '';
      this.screenshot = null;
    },
    validateUrl(url) {
      const urlRegex = /^(ftp|http|https):\/\/[^ "]+$/;
      return urlRegex.test(url) && url.length <= 256;
    },
    generateShortUrl() {
      const isValidUrl = this.validateUrl(this.url);
      if (!isValidUrl) {
        this.errorMessage = 'You entered invalid URL or the URL is too long. Please check and try again!';
        return;
      }
      this.showProgressBar = true;
      const headers = {
        'Content-Type': 'application/json;charset=UTF-8',
        'Access-Control-Allow-Origin': '*',
      }
      axios.post('http://localhost:5000/saveurl', {url: this.url}, {headers})
      .then(response => {
        this.shortUrl = response.data.shortUrl;
        this.screenshot = response.data.screenshot;
      })
      .catch(error => {
        this.errorMessage = error.response.data.message;
      })
      .finally(()=>{
        this.showProgressBar = false;
      })
    },
    getImageUrl(filename) {
      return require(`@/assets/images/${filename}`);
    }
  },
  components: {
    InputField,
    ShortUrlField,
    ErrorAlert
  }
};
</script>

<style>
  #generate_button{
    align-self: center;
    padding: 8px;
    background-color: aquamarine;
    border-radius: 30px;
    border: none;
    cursor: pointer;
    margin-bottom: 20px;
  }
  .firstUrl_input{
    margin-bottom: 15px;
  }
  .shortUrl_result{
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
  }
  .shortUrl_link{
    margin-bottom: 20px;
  }
</style>