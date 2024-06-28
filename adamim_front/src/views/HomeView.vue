<template>
  <div class="home">

<div class="hero has-background-primary-light mb-6 pl-3">
  <div class="hero-content">
    <div class="left-content">
      <router-link to="/">
        <a>
          <img src="@/assets/logo.png" alt="Logo kalima">
        </a>
      </router-link>
    </div>
    <div class="right-content" style="text-align: center;">
      <h2>Welcome to</h2>
      <h1 class="main_title" style="letter-spacing: -5px;">Kalima</h1>
      <h2>Your destination for Arabic manuscript OCR</h2>
    </div>
  </div>
</div>
    

    <div class="tile is-ancestor mb-3" style="box-shadow: 0 0 10px rgba(0, 0, 0, 0.1); background-color: #3d5a80;">
  <div class="tile is-4 is-vertical is-parent">
    <div class="tile is-child has-background-primary-light box" style="box-shadow: 0 0 10px rgba(0, 0, 0, 0.1); background-color: #8ecae6;">
      
        <h3 class="title is-size-3">What is Kalima ?</h3>
        <p class="main_content is-size-5" style="letter-spacing: 1px;">
            Kalima is a powerful tool designed to extract text from Arabic manuscripts using Optical Character Recognition (OCR) technology.
        </p>
        <br>
        <p class="main_content is-size-5" style="letter-spacing: 1px;">
            With Kalima, you can easily digitize and analyze ancient Arabic texts, making them accessible for research, education, and preservation purposes.
        </p>
    </div>
    <div class="tile is-child has-background-primary-light box" style="box-shadow: 0 0 10px rgba(0, 0, 0, 0.1); background-color: #8ecae6;">
    
      <h3 class="title is-size-3">Key Features</h3>
          <ul class="main_content">
            <li><i class="fa-regular fa-square-check" style="color: #006106;"></i> Accurate OCR for Arabic manuscripts</li>
            <br>
            <li><i class="fa-regular fa-square-check" style="color: #006106;"></i> Supports various manuscript formats</li>
            <br>
            <li><i class="fa-regular fa-square-check" style="color: #006106;"></i> Easy-to-use interface</li>
            <br>
            <li><i class="fa-regular fa-square-check" style="color: #006106;"></i> Customizable output options</li>
            <br>
            <li><i class="fa-regular fa-square-check" style="color: #006106;"></i> Advanced text analysis tools</li>
            <br>
            <li><i class="fa-regular fa-square-check" style="color: #006106;"></i> Integration with machine learning models for enhanced accuracy</li>
            <br>
            <li><i class="fa-regular fa-square-check" style="color: #006106;"></i> Scalable solution for processing large volumes of manuscripts</li>
            <br>
          </ul>
    </div>
  </div>
  <div class="tile is-parent">
    <div class="tile is-child has-background-primary-light box" style="box-shadow: 0 0 10px rgba(0, 0, 0, 0.1); background-color: #8ecae6;">
    
      <figure class="image">
      <img src="@/assets/Innovation-amico.png">
    </figure>
    </div>
  </div>
</div>
<br> <br>

<section class="hero has-background-info-dark" style="text-align: center; border-radius: 15px; font-family: 'inter', sans-serif; box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);">
  <div class="hero-body" style="color: white;">
    <p class="her_title" style="font-size: 250%;">
      Get Started
    </p>
    <br>
    <p class="hero_subtitle" style="font-size: 150%;">
      Ready to explore the world of Arabic manuscript OCR? Sign up now to get started!
    </p>
    <br>
    <router-link to="/Api" class="button is-primary is-size-5">Access Kalima</router-link>
  </div>
</section>
</div>

</template>

<script>
export default {
  mounted() {
    document.title = 'Welcome To Kalima';
  }
};
</script>

<style scoped>


.home {
  position: relative;
}

.background-gif img {
  width: 100%;
}

.banner {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  text-align: center;
  z-index: 1;
}

.banner-title,
.banner-subtitle {
  color: #fff;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
}

.content {
  position: relative;
  z-index: 2;
}

.home {
  background: none;
  border-radius: 20px;
}

.hero-content {
  display: flex;
  align-items: center;
}

div{
border-radius: 16px;
}
.left-content {
  margin-right: 150px; /* Adjust as needed */
}

.right-content {
  /* text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5); Add shadow to the text */
  font-size: 2em;
  font-weight: bold;
  color: #00008B;
}

.main_title {
  font-size: 3em;
  font-weight: bold;
  color: #00008B;
  font-family: 'inter', sans-serif;
}

.title{
  color: #00008B;
  font-family: 'inter', sans-serif;
  font-weight: 800;
}

.main_content{
  font-family: 'inter', sans-serif;
  color: #00008B;
}



</style>
