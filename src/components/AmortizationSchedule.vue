<template>
  <v-dialog v-model="dialog" width="400">
    <template v-slot:activator="{ on, attrs }">
      <v-btn
        v-on:click="calc_payments"
        color="blue"
        v-bind="attrs"
        v-on="on"
        small
      >
        Details
      </v-btn>
    </template>

    <v-card>
      <v-card-title class="headline grey lighten-2">
        <div v-if="payments.length">
          <h6>
            Monthly principal & interest:
            {{ monthlyPayment.toFixed(2) }}
          </h6>
          <h6>Total Interest: {{ totalInterest.toFixed(2) }}</h6>
          <h6>Total of all monthly payments: {{ totalPayment.toFixed(2) }}</h6>
        </div>
      </v-card-title>

      <v-card-text>
        <table class="table" cellspacing="10" v-if="payments.length">
          <thead>
            <tr>
              <th>Number</th>
              <th>Payment</th>
              <th>Interest</th>
              <th>Principal</th>
              <th>Balance</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="payment in payments" :key="payment.count">
              <td>{{ payment.count }}</td>
              <td>{{ payment.payment.toFixed(2) }}</td>
              <td>{{ payment.interest.toFixed(2) }}</td>
              <td>{{ payment.principal.toFixed(2) }}</td>
              <td>{{ payment.balance.toFixed(2) }}</td>
            </tr>
          </tbody>
        </table>
      </v-card-text>

      <v-divider></v-divider>

      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn color="primary" text @click="dialog = false"> Close </v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script type="text/javascript">
export default {
  data() {
    return {
      interestRate: 15,
      payments: [],
      dialog: false,
    };
  },
  props: ["loanAmount", "paymentNumber"],
  methods: {
    reset() {
      this.interestRate = "";
      this.monthlyPayment = "";
      this.payments = [];
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