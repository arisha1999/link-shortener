<template>
    <transition name="error-alert">
      <div class="error-alert" v-if="errorMessage">
        <v-alert
          title="Error"
          :text="errorMessage"
          variant="outlined"
        ></v-alert>
      </div>
    </transition>
  </template>
  
  <script>
  export default {
    props: {
      errorMessage: {
        type: String,
        default: ''
      }
    }
  }
  </script>
  
  <style scoped>
  .error-alert {
    position: fixed;
    top: 30px;
    left: 0;
    right: 0;
    z-index: 9999;
    display: flex;
    justify-content: center;
    align-items:center;
    max-width: 25%;
    margin: 0 auto;
  }
  
  .v-alert {
    background-color: rgb(245, 81, 81);
    color: white;
    padding: 15px;
    margin-bottom: 10px;
  }
  </style>
  