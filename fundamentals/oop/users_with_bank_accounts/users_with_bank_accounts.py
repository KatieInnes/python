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



class User: 
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)

    # Add a make_deposit method to the User class that calls on it's bank account's instance methods.
    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self
    
    # Add a make_withdrawal method to the User class that calls on it's bank account's instance methods.
    def make_withdrawl(self, amount):
        self.account.withdraw(amount)
        return self
    
    # Add a display_user_balance method to the User class that displays user's account balance.
    def display_user_balance(self):
        self.account.display_account_info()
        return self

    
santaclaus = User("Santa Claus", "santa@np.com")
easterbunny = User("Easter Bunny", "eb@spring.com")


santaclaus.make_deposit(350).display_user_balance()
easterbunny.make_deposit(100).make_withdrawl(50).make_withdrawl(60).display_user_balance()
