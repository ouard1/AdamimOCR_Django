<template>
    <div class="page-sign-up">
        <div class="columns">
            <div class="column is-4 is-offset-4">
                <h1 class="title">Log in</h1>

                <form @submit.prevent="submitForm">
                    <div class="field">
                        <label>Username</label>
                        <div class="control">
                            <input type="text" class="input" v-model="username">
                        </div>
                    </div>

                    <div class="field">
                        <label>Password</label>
                        <div class="control">
                            <input type="password" class="input" v-model="password">
                        </div>
                    </div>

                    <div class="notification is-danger" v-if="errors.length">
                        <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                    </div>

                    <div class="field">
                        <div class="control">
                            <button class="button is-link">Log in</button>
                        </div>
                    </div>
                    
                    <GoogleLogin :callback="callback" @googleLoginSuccess="handleGoogleLoginSuccess"/>


                    <hr>
                    <p>Or</p>
                    <router-link to="/sign-up" @click="closeModal">Click Here</router-link> To Sign up !
                    
                </form>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    name: 'Login',
    data() {
        return {
            username: '',
            password: '',
            errors: []
        };
    },
    methods: {
        async submitForm() {
            try {
                const formData = {
                    username: this.username,
                    password: this.password
                };
                const response = await axios.post("/api/v1/token/login/", formData);
                const token = response.data.auth_token;

                this.handleLoginSuccess(token);
            } catch (error) {
                this.handleLoginError(error);
            }
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
        closeModal() {
            this.$emit('closeModal');
        },
        handleGoogleLoginSuccess() {
            this.$router.push('/api');
        }
    }
}
</script>

