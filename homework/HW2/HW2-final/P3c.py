def make_withdrawal(balance):
    def withdraw(amount):
        nonlocal balance
        balance = balance - amount
        if balance < 0:
            raise ValueError
        return balance
    return withdraw

wd = make_withdrawal(100)
print(wd(50)) 
print(wd(10)) 
