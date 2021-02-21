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
// import axios from "axios";
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
      let payload = {
          username: this.username,
          password: this.password,
      };
      this.$backend.$login(payload).then((res) => {
        console.log(res)
        if (res.status == 200) {
          this.token = res.data.token;
          localStorage.setItem("user-token", res.data.token);
					localStorage.setItem("is-admin", res.data.admin);
          this.$router.push("/");
        }
      });
    },
  },
};
</script>