<template>
  <div v-if="isAuthenticated" class="my_api">
    <iframe
      ref="iframe"
      :src="iframeSrc"
      width="850"
      height="600"
      frameborder="0"
      style="border-radius: 15px; overflow: hidden;"
    ></iframe>
  </div>
  <div v-else>
    <p>You are not authenticated.</p>
  </div>
</template>

<script>
export default {
  name: 'Api',
  data() {
    return {
      isAuthenticated: false
    };
  },
  mounted() {
    this.checkAuthentication();
  },
  methods: {
    checkAuthentication() {
      // Check if the user is authenticated (you need to implement this logic)
      const token = localStorage.getItem("token");
      if (token) {
        // User is authenticated, redirect to the Hugging Face Space
        const url = `https://huggingface.co/spaces/RamyBTG/AdamimOCR?access_token=${token}`;
        window.location.href = url;
      } else {
        // User is not authenticated, you may want to handle this case differently
        console.error("User is not authenticated");
      }
    }
  }
}
</script>

<style scoped>
/* Your component-specific styles */
.my_api {
  display: flex;
  justify-content: center;
}
</style>
