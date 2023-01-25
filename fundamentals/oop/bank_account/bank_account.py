class BankAccount:
    account_info = []

    def __init__(self, int_rate, balance = 0): 
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.account_info.append(self)

    # increases the account balance by the given amount
    def deposit(self, amount):
        self.balance = self.balance + amount
        return self

    # decreases the account balance by the given amount if there are sufficient funds; if there is not enough money, print a message "Insufficient funds: Charging a $5 fee" and deduct $5
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance = self.balance - amount
        else:
            self.balance = self.balance - 5
            print("Insufficient funds: Charging a $5 fee")
        return self

    # print to the console: eg. "Balance: $100"
    def display_account_info(self):
        print(f"Balance: $", self.balance)
        return self
        
    # increases the account balance by the current balance * the interest rate (as long as the balance is positive)
    def yield_interest(self):
        if self.balance > 0:
            self.balance = self.balance * (1 + self.int_rate)
        else:
            print("No interest may be accrued on zero-balance accounts")
        return self

    # NINJA BONUS: use a classmethod to print all instances of a Bank Account's info
    @classmethod
    def print_all_account_info(cls):
        for account in cls.account_info:
            account.display_account_info()

# Create two accounts
account1 = BankAccount(0.011, 100)
account2 = BankAccount(0.015, 1000)

# To the first account, make 3 deposits and 1 withdrawal, then yield interest and display the account's info all in one line of code (i.e. chaining)
account1.deposit(300).deposit(500).deposit(1000).withdraw(1200).display_account_info()

# To the second account, make 2 deposits and 4 withdrawals, then yield interest and display the account's info all in one line of code (i.e. chaining)
account2.deposit(1000).deposit (3500).withdraw(800).withdraw(250).withdraw(3650).withdraw(2000).yield_interest().display_account_info()

# NINJA BONUS: use a classmethod to print all instances of a Bank Account's info
BankAccount.print_all_account_info()