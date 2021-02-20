<template>
  <v-app id="inspire">
    <v-layout class="mt-8 mb-5" justify-center>
      <v-flex xs3>
        <v-text-field
          label="Amount"
          type="number"
          v-model="loanAmount"
        ></v-text-field>
        <v-text-field
          label="Term in Years"
          type="number"
          v-model="paymentNumber"
        >
        </v-text-field>
        <div class="mt-5">
          <amortization-schedule
            v-bind:loanAmount="loanAmount"
            v-bind:paymentNumber="paymentNumber"
          />
          <v-btn
            small
            color="success"
            class="ml-5"
            @click="postLoan"
            :disabled="!loanAmount || !paymentNumber"
          >
            Request
          </v-btn>
        </div>
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

<script type="text/javascript">
import AmortizationSchedule from "./AmortizationSchedule.vue";
export default {
  mounted() {},
  data() {
    return {
      loanAmount: "",
      paymentNumber: "",
      interestRate: 15,
      payments: [],
      dialog: false,
      snackbar: false,
      text: "",
    };
  },
  components: {
    AmortizationSchedule,
  },
  methods: {
    reset() {
      this.loanAmount = "";
      this.paymentNumber = "";
      this.interestRate = "";
      this.monthlyPayment = "";
      this.payments = [];
    },
    postLoan() {
      let axiosConfig = {
        headers: {
          Authorization: "Token " + localStorage.getItem("user-token"),
        },
      };
      const payload = { amount: this.loanAmount, term: this.paymentNumber };
      this.$backend.$postLoan(payload, axiosConfig).then((response) => {
        if (response.status == 200) {
          this.text = response.data.message;
          this.snackbar = true;
          this.$emit('appendLoan', response.data.result)
        } else {
          this.text = `Something went wrong!`;
          this.snackbar = true;
        }
        this.paymentNumber = "";
        this.loanAmount = "";
      });
    },
    calc_payment(
      p = this.loanAmount,
      n = this.paymentNumber * 12,
      int = this.interestRate
    ) {
      let r = int / 100 / 12;
      let pmt = p * ((r * Math.pow(1 + r, n)) / (Math.pow(1 + r, n) - 1));
      this.monthlyPayment = pmt;
      return pmt;
    },
    calc_payments(
      e,
      balance = parseFloat(this.loanAmount),
      rate = this.interestRate
    ) {
      var count = 0;
      var payments = [];
      var totalPayment = 0;
      var totalInterest = 0;
      let payment = Number(this.calc_payment());
      do {
        count++;
        var interest = balance * (rate / 12 / 100);
        var principal = payment - interest;
        if (balance < payment) {
          principal = balance;
          payment = Number(interest) + Number(principal);
        }
        balance = balance - principal;
        if (balance < 0) {
          principal = principal + balance;
          interest = Number(interest) - balance;
          balance = 0;
        }
        payments.push({
          balance: balance,
          payment: payment,
          interest: interest,
          principal: principal,
          count,
        });
        totalPayment = totalPayment + payment;
        totalInterest = totalInterest + interest;
      } while (balance > 0);
      this.payments = payments;
      this.totalInterest = totalInterest;
      this.totalPayment = totalPayment;
    },
  },
};
</script>

<style type="text/css" scoped>
table {
  margin-top: 5%;
  border-top: 1px solid #ccc;
}
input {
  max-width: 100px;
}
.row {
  display: flex;
  flex-direction: column;
}
</style>