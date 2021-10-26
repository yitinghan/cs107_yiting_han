from Bank import BankUser
from Bank import AccountType
from Bank import BankAccount


def test_over_withdrawal():  # this test function should throw an Exception or Error
    user = BankUser("Joe")
    user.addAccount(AccountType.SAVINGS)
    user.deposit(AccountType.SAVINGS, 10)
    try:
        # this will cause an Exception or Error
        user.withdraw(AccountType.SAVINGS, 1000)
    except Exception as e:
        print(e)  # print the message for the Exeption


def test_negative_withdrawal():  # this test function should throw an Exception or Error
    user = BankUser("Joe")
    user.addAccount(AccountType.SAVINGS)
    user.deposit(AccountType.SAVINGS, 10)
    try:
        # this will cause an Exception or Error
        user.withdraw(AccountType.SAVINGS, -10)
    except Exception as e:
        print(e)  # print the message for the Exeption


def test_negative_deposit():  # this test function should throw an Exception or Error
    user = BankUser("Joe")
    user.addAccount(AccountType.SAVINGS)
    user.deposit(AccountType.SAVINGS, 10)
    try:
        # this will cause an Exception or Error
        user.deposit(AccountType.SAVINGS, -10)
    except Exception as e:
        print(e)  # print the message for the Exeption


def test_duplicated_savings():  # this test function should throw an Exception or Error
    user = BankUser("Joe")
    user.addAccount(AccountType.SAVINGS)
    try:
        # this will cause an Exception or Error
        user.addAccount(AccountType.SAVINGS)
    except Exception as e:
        print(e)  # print the message for the Exeption


def test_duplicated_checking():  # this test function should throw an Exception or Error
    user = BankUser("Joe")
    user.addAccount(AccountType.CHECKING)
    try:
        # this will cause an Exception or Error
        user.addAccount(AccountType.CHECKING)
    except Exception as e:
        print(e)  # print the message for the Exeption


def test_no_account():  # this test function should throw an Exception or Error
    user = BankUser("Joe")
    user.addAccount(AccountType.SAVINGS)
    try:
        # this will cause an Exception or Error
        user.deposit(AccountType.CHECKING, 10)
    except Exception as e:
        print(e)  # print the message for the Exeption


def test_deposit_withdraw():
    user = BankUser("Joe")
    user.addAccount(AccountType.SAVINGS)
    user.addAccount(AccountType.CHECKING)
    user.deposit(AccountType.SAVINGS, 100)
    user.deposit(AccountType.CHECKING, 100)

    try:
        user.withdraw(AccountType.SAVINGS, 10)
        print(user)
    except Exception as e:
        print(e) 


test_over_withdrawal()
test_negative_withdrawal()
test_negative_deposit()
test_duplicated_savings()
test_duplicated_checking()
test_no_account()
test_deposit_withdraw()