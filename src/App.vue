<template>
  <v-app>
    <v-app-bar app color="primary" dark>
      <div class="d-flex align-center"><h2>Loan Management App</h2></div>

      <v-spacer></v-spacer>

      <div v-if="token == null">
        <v-btn class="mr-1">
          <router-link :to="{ name: 'register' }">Register</router-link>
        </v-btn>
        <v-btn>
          <router-link :to="{ name: 'login' }">Login</router-link>
        </v-btn>
      </div>
      <v-btn v-on:click="logout" v-if="token !== null">Logout</v-btn>
    </v-app-bar>

    <v-main>
      <div v-if="token !== null">
        <div v-if="isAdmin == 'true'">
          <PendingLoans />
        </div>
        <div v-else-if="isAdmin == 'false'">
          <Loans />
        </div>
      </div>
      <router-view />
    </v-main>
  </v-app>
</template>

<script>
import Loans from "@/components/Loans.vue";
import PendingLoans from "@/components/PendingLoans.vue";
export default {
  name: "App",
  components: {
    Loans,
    PendingLoans,
  },
  data: () => ({
    token: localStorage.getItem("user-token") || null,
    isAdmin: localStorage.getItem("is-admin") || null,
  }),
  methods: {
    logout() {
      localStorage.removeItem("user-token");
      localStorage.removeItem("is-admin");
      this.token = null;
      this.isAdmin = null;
    },
  },
  watch: {
    $route() {
      this.token = localStorage.getItem("user-token") || null;
      this.isAdmin = localStorage.getItem("is-admin") || null;
    },
  },
};
</script>
