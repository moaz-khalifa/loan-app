<template>
  <v-layout justify-center>
    <v-flex xs4>
      <h1 class="mt-8 mb-5">Login</h1>
      <form id="formvideo" @submit.prevent="login">
        <v-text-field label="Username" v-model="username"></v-text-field>
        <v-text-field
          label="password"
          type="password"
          v-model="password"
        ></v-text-field>
        <v-card-actions class="justify-center">
          <v-btn type="submit" value="Submit" :disabled="!password || !username"
            >Login
          </v-btn>
        </v-card-actions>
      </form>
    </v-flex>
  </v-layout>
</template>

<script>
// @ is an alias to /src
import axios from "axios";
export default {
  name: "Login",
  components: {},
  data() {
    return {
      username: "",
      password: "",
      token: localStorage.getItem("user-token") || null,
    };
  },
  methods: {
    login() {
      axios
        .post("http://127.0.0.1:8000/api-token-auth/", {
          username: this.username,
          password: this.password,
        })
        .then((resp) => {
          this.token = resp.data.token;
          localStorage.setItem("user-token", resp.data.token);
					localStorage.setItem("is-admin", resp.data.admin);
          this.$router.push("/");
        })
        .catch((err) => {
          localStorage.removeItem("user-token");
          console.log(err);
        });
    },
  },
};
</script>