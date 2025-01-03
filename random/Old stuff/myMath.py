class Finance():
    def isprime(self, nums: int) -> int:
        if nums <= 1:
            return None
        for i in range(2, nums):
            if nums % i == 0:
                return None
        return nums

    def present_value_bond(self, interest: bool, coupon: bool, face_value: int, n_term: int) -> int:
        self.interest = interest
        self.coupon = coupon
        self.face_value = face_value
        self.n_term = n_term
        fv_table1 = (1 + interest) ** n_term
        fv_table2 = ((1 + interest) ** n_term - 1) / interest
        pv_table3 = 1 / (1 + interest) ** n_term
        pv_interest_table4 = (1 - 1 / (1 + interest) ** n_term) / interest

        pv_maturity = face_value / (1 + interest) ** n_term
        interest_payment = face_value * coupon
        pv_interest_payment = interest_payment * pv_interest_table4
        print(pv_interest_payment)

    def prof_trading_crypto(self, captital: int, fee: int, r: float) -> float:
        initial = (1 - fee) * captital
        return -initial + initial * (1 + r) - fee * initial * (1 + r)


question = Finance()
question.present_value_bond(0.16, 0.1, 20000, 19)

print(question.prof_trading_crypto(1000, 0.02, .09))
