from enum import Enum

class AccountType(Enum):
    SAVINGS = 1
    CHECKING = 2

class BankAccount():
    
    def __init__(self, owner, accountType: AccountType):
        self.owner = owner
        self.accountType = accountType
        self.balance = 0

    def withdraw(self, amount):
        if amount < 0:
            raise Exception("You cannot withdraw a negative amount.")
        if amount > self.balance:
            raise Exception("You cannot withdraw more money than your current balance.")
        self.balance -= amount
        
    def deposit(self, amount):
        if amount < 0:
            raise Exception("You cannot deposit a negative amount.")
        self.balance += amount

    def __str__(self):
        return f"Account owner: {self.owner} \n" \
               f"Account type: {self.accountType.name} \n " \
               f"Balance: {self.balance}"

    def __len__(self):
        return self.balance


class BankUser():
    
    def __init__(self, owner):
        self.owner = owner
        self.accounts = {}
    
    def addAccount(self, accountType):
        if accountType.name in self.accounts:
            raise Exception(f"You have a {accountType.name} account already.")
        self.accounts[accountType.name] = BankAccount(self.owner, accountType)

    def getBalance(self, accountType):
        if accountType.name not in self.accounts:
            raise Exception(f"You do not have a {accountType.name} account.")
        return len(self.accounts[accountType.name])
        
    def deposit(self, accountType, amount):
        if accountType.name not in self.accounts:
            raise Exception(f"You do not have a {accountType.name} account.")
        self.accounts[accountType.name].deposit(amount)

    def withdraw(self, accountType, amount):
        if accountType.name not in self.accounts:
            raise Exception(f"You do not have a {accountType.name} account.")
        self.accounts[accountType.name].withdraw(amount)

    def __str__(self):
        output = f"Bank user: {self.owner} \n"
        for account in self.accounts:
            output += account + ": " + str(len(self.accounts[account]))+ " \n"
        return output


def ATMSession(bankUser):
    def Interface():
        while True:
            print("Enter Option:")
            print("1)Exit")
            print("2)Create Account")
            print("3)Check Balance")
            print("4)Deposit")
            print("5)Withdraw")
            firstChoice = input()

            if firstChoice == "1":
                break
            else:
                print("Enter Option:")
                print("1)Checking")
                print("2)Savings")
                secondChoice = input()
                while secondChoice != "1" and secondChoice != "2":
                    secondChoice = input("Sorry you have to choose between 1 and 2")

                if firstChoice == "2":
                    if secondChoice == "1":
                        try:
                            bankUser.addAccount(AccountType.CHECKING)
                        except Exception as e:
                            print(e)
                    else:
                        try:
                            bankUser.addAccount(AccountType.SAVINGS)
                        except Exception as e:
                            print(e)
                elif firstChoice == "3":
                    if secondChoice == "1":
                        try:
                            balance = bankUser.getBalance(AccountType.CHECKING)
                            print(f"Current balance of your checking account: {str(balance)}")
                        except Exception as e:
                            print(e)
                    else:
                        try:
                            balance = bankUser.getBalance(AccountType.SAVINGS)
                            print(f"Current balance of your savings account: {str(balance)}")
                        except Exception as e:
                            print(e)
                elif firstChoice == "4":
                    print("Enter Integer Amount, Cannot Be Negative: ")
                    amount = int(input())
                    if secondChoice == "1":
                        try:
                            bankUser.deposit(AccountType.CHECKING, amount)
                        except Exception as e:
                            print(e)
                    else:
                        try:
                            bankUser.getBalance(AccountType.SAVINGS, amount)
                        except Exception as e:
                            print(e)
                elif firstChoice == "5":
                    print("Enter Integer Amount, Cannot Be Negative:")
                    amount = int(input())
                    if secondChoice == "1":
                        try:
                            bankUser.withdraw(AccountType.CHECKING, amount)
                        except Exception as e:
                            print(e)
                    else:
                        try:
                            bankUser.withdraw(AccountType.SAVINGS, amount)
                        except Exception as e:
                            print(e)

    return Interface


# user = BankUser("Joe")
# session = ATMSession(user)
# session()
