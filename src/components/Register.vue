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
    <v-snackbar v-model="snackbar">
      {{ text }}

      <template v-slot:action="{ attrs }">
        <v-btn color="pink" text v-bind="attrs" @click="snackbar = false">
          Close
        </v-btn>
      </template>
    </v-snackbar>
  </div>
</template>

<script>
export default {
  name: "register",
  components: {},
  data() {
    return {
      username: null,
      password: null,
      email: null,
      snackbar: false,
      text: "",
    };
  },
  methods: {
    CreateUser() {
      let payload = { 
          username: this.username,
          password: this.password,
          email: this.email,
      };
      this.$backend.$register(payload).then((res) => {
        console.log(res.status)
        if (res.status == 201) {
          this.text = 'User created successfully, please log in!';
          this.snackbar = true;
          this.username = null,
          this.password = null,
          this.email = null
        }
      });
    },
  },
};
</script>