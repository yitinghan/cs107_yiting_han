def make_withdrawal(balance):
    def withdraw(amount):
        balance = balance - amount
        if balance < 0:
            raise ValueError
        return balance
    return withdraw


print(
"It throws an UnboundLocalError because \n" +  
"local variable 'balance' referenced before assignment. ")

wd = make_withdrawal(100)
print(wd(50)) 
print(wd(60)) 
