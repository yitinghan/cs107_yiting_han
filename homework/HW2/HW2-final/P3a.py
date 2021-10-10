def make_withdrawal(balance):
    def withdraw_money(withdraw_amount):
        if withdraw_amount > balance:
            raise ValueError
        return balance - withdraw_amount


    return withdraw_money

init_balance = 100
withdrawal_amount = 10
new_withdrawal_amount = 20
wd = make_withdrawal(init_balance)


print("Explanation:  We didn't update the value of balance in the inner function. Therefore, when we run the inner function \n"
      "multiple times, the balance comes from its parent scope and it remains unchanged"
      )
print(wd(withdrawal_amount))
print(wd(new_withdrawal_amount))
