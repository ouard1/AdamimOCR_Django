<template>
    <div class="page-sign-up">
        <div class="columns">
            <div class="column is-4 is-offset-4">
                <h1 class="title" style="color: aliceblue;">Log in</h1>

                <form @submit.prevent="submitForm">
                    <div class="field">
                        <label class="label">Username</label>
                        <div class="control">
                            <input type="text" class="input" v-model="username">
                        </div>
                    </div>

                    <div class="field">
                        <label class="label">Password</label>
                        <div class="control">
                            <input type="password" class="input" v-model="password">
                        </div>
                    </div>

                    <div class="notification is-danger" v-if="errors.length">
                        <p v-for="error in errors" v-bind::key="error">{{ error }}</p>
                    </div>

                    <div class="field">
                        <div class="control">
                            <button class="button is-link">Log in</button>
                        </div>
                    </div>

                    <hr>

                    <div style="font-family: 'poppins', sans-serif; color: white; text-align: center;">
                        or sign up with Google 
                        <img src="@/assets/google.png" alt="Google Sign Up" style="width: 1.5em; height: 1.5em; margin-left: 5px; background: transparent;"/>
                    </div>
                    <br>
                    <div style="display: flex; justify-content: center;">
                    <GoogleLogin :callback="callback" @googleLoginSuccess="handleGoogleLoginSuccess"/>
                    </div>
                    
                </form>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
export default{
    name: 'Login',
    data(){
        return{
            username: '',
            password: '',
            errors: []
        }
    },
mounted(){
    document.title = 'log In | Adamim OCR'
},
methods: {
    async submitForm(){
        axios.defaults.headers.common["Authorization"] = ""

        localStorage.removeItem("token")

        const formData = {
            username: this.username,
            password: this.password
        }

        await axios
            .post("/api/v1/token/login/", formData)
            .then(response => {
                const token = response.data.auth_token

                this.$store.commit('setToken', token)

                axios.defaults.headers.common["Authorization"] = "Token " + token

                localStorage.setItem("token", token)

                // const toPath = this.$route.query.to || '/Api'

                this.$router.push('/Api')

            })
            .catch(error => {
                if (error.response){
                    for (const property in error.response.data){
                        this.errors.push(`${property}: ${error.response.data[property]}`)
                    }
                } else {
                    this.errors.push("Something went wrong. Please try again")
                    
                    console.log(JSON.stringify(error))
                }
            })
        
    },
    async handleLoginSuccess(token) {
            localStorage.setItem("token", token);
            axios.defaults.headers.common["Authorization"] = "Token " + token;
            window.location.href = '/Api';
            this.$emit('closeModal');
        },
        handleLoginError(error) {
            if (error.response) {
                for (const property in error.response.data) {
                    this.errors.push(`${property}: ${error.response.data[property]}`);
                }
            } else {
                this.errors.push("Something went wrong. Please try again");
                console.error(JSON.stringify(error));
            }
        },
        callback(response) {
            if (response.clientId && response.client_id && response.credential && response.select_by) {
                const token = response.credential;
                const expirationTime = new Date().getTime() + 30 * 60 * 1000;
                localStorage.setItem('token', JSON.stringify({ token, expirationTime }));

                this.handleLoginSuccess(token);
            } else {
                console.error('Invalid response from Google authentication');
            }
        },
        handleGoogleLoginSuccess() {
            this.$router.push('/api');
        }
}
}

</script>

<style>
.label{
    color: white;
}

img{
    background: transparent;
}
</style>