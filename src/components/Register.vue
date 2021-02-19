<template>
  <div class="">
    <v-layout justify-center>
      <v-flex xs4>
				<h1 class='mt-8 mb-5'>Sign Up</h1>
        <form id="formvideo" @submit.prevent="CreateUser">
          <v-text-field label="Username" v-model="username"></v-text-field>
          <v-text-field
            label="Email"
            type="email"
            v-model="email"
          ></v-text-field>
          <v-text-field
            label="password"
            type="password"
            v-model="password"
          ></v-text-field>
          <v-card-actions class="justify-center">
            <v-btn
              type="submit"
              value="Submit"
              :disabled="!password || !email || !username"
              >Register
            </v-btn>
          </v-card-actions>
        </form>
      </v-flex>
    </v-layout>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "register",
  components: {},
  data() {
    return {
      username: null,
      password: null,
      email: null,
    };
  },
  methods: {
    CreateUser() {
      axios
        .post("http://127.0.0.1:8000/api/users/", {
          username: this.username,
          password: this.password,
          email: this.email,
        })
        .then((res) => console.log(res))
        .catch((err) => console.log(err));
      this.$router.push("/");
    },
  },
};
</script>