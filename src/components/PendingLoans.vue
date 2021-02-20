<template>
  <v-app id="inspire">
    <v-layout justify-center>
      <v-flex xs8>
        <v-simple-table>
          <template v-slot:default>
            <thead>
              <h2 class="mt-8 mb-5">Pending Loans</h2>
              <tr>
                <th class="text-left">Amount</th>
                <th class="text-left">Term (in years)</th>
                <th class="text-left">Customer</th>
                <th class="text-left">Created At</th>
                <th class="text-left">Action</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(loan, index) in loans" :key="index">
                <td>{{ loan.amount }}</td>
                <td>{{ loan.term }}</td>
                <td>{{ loan.user }}</td>
                <td>{{ format_date(loan.created) }}</td>
                <td>
                  <v-btn
                    class="mr-1"
                    color="success"
                    small
                    @click="updateLoan(loan.id, 'approved')"
                    >Approve
                  </v-btn>
                  <v-btn
                    class="mr-1"
                    color="error"
                    small
                    @click="updateLoan(loan.id, 'rejected')"
                    >Reject
                  </v-btn>
                  <amortization-schedule
                    v-bind:loanAmount="loan.amount"
                    v-bind:paymentNumber="loan.term"
                  />
                </td>
              </tr>
            </tbody>
          </template>
        </v-simple-table>
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
  </v-app>
</template>

<script>
import moment from "moment";
import AmortizationSchedule from "./AmortizationSchedule.vue";
export default {
  name: "PendingLoans",
  components: {
    AmortizationSchedule,
  },
  data() {
    return {
      loans: [],
      snackbar: false,
      text: "",
    };
  },
  mounted() {
    this.fetchPendingLoans();
  },
  methods: {
    fetchPendingLoans() {
      let axiosConfig = {
        headers: {
          Authorization: "Token " + localStorage.getItem("user-token"),
        },
      };
      this.$backend.$fetchPendingLoans(axiosConfig).then((responseData) => {
        this.loans = responseData;
      });
    },
    updateLoan(id, status) {
      let axiosConfig = {
        headers: {
          Authorization: "Token " + localStorage.getItem("user-token"),
        }
      };
      let payload = { status: status };
      this.$backend.$updateLoan(id, payload, axiosConfig).then((response) => {
        console.log(response)
        if (response.status == 200) {
          this.text = `The loan has been successfully ${status}`;
          this.snackbar = true;
        } else {
          this.text = `Something went wrong!`;
          this.snackbar = true;
        }
        this.fetchPendingLoans();
      });
    },
    format_date(value) {
      if (value) {
        return moment(String(value)).format("DD/MM/YYYY HH:mm");
      }
    },
  },
};
</script>