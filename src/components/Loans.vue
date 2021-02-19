<template>
  <v-app id="inspire">
    <v-tabs vertical>
      <v-tab> Request a Loan </v-tab>
      <v-tab> My Loans </v-tab>
      <v-tab-item>
        <v-card flat>
          <v-card-text>
            <loan-handler />
          </v-card-text>
        </v-card>
      </v-tab-item>
      <v-tab-item>
        <v-card flat>
          <v-card-text>
            <v-layout justify-center>
              <v-flex xs8>
                <v-simple-table>
                  <template v-slot:default>
                    <thead>
                      <h2 class="mt-8 mb-5">My Loans</h2>
                      <tr>
                        <th class="text-left">Amount</th>
                        <th class="text-left">Term (in years)</th>
                        <th class="text-left">Status</th>
                        <th class="text-left">Created At</th>
                        <th></th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr v-for="(loan, index) in loans" :key="index">
                        <td>{{ loan.amount }}</td>
                        <td>{{ loan.term }}</td>
                        <td>{{ loan.status.toUpperCase() }}</td>
                        <td>{{ format_date(loan.created) }}</td>
                        <td>
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
          </v-card-text>
        </v-card>
      </v-tab-item>
    </v-tabs>
  </v-app>
</template>

<script>
import moment from "moment";
import LoanHandler from "./LoanHandler.vue";
import AmortizationSchedule from "./AmortizationSchedule.vue";
export default {
  name: "Loans",
  components: {
    LoanHandler,
    AmortizationSchedule
  },
  data() {
    return {
      amount: "",
      term: "",
      loans: [],
      tab: null,
      items: ["Request a Loan", "My Loans"],
    };
  },
  mounted() {
    this.fetchLoans();
  },
  methods: {
    fetchLoans() {
      this.$backend.$fetchLoans().then((responseData) => {
        this.loans = responseData;
      });
    },
    postLoan() {
      let axiosConfig = {
        headers: {
          Authorization: "Token " + localStorage.getItem("user-token"),
        },
      };
      const payload = { amount: this.amount, term: this.term };
      this.$backend.$postLoan(payload, axiosConfig).then(() => {
        this.term = "";
        this.amount = "";
        this.fetchLoans();
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