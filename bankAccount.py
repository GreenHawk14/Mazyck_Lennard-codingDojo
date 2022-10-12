class BankAccount:
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance):
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon
        self.int_rate = int_rate
        self.balance = balance
    def deposit(self, amount):
        # your code here
        print(self.balance)
        self.balance = amount
        deposit_amt = int(input("How much money do you wish to deposit: "))
        amount = amount + deposit_amt
        return self
    def withdraw(self, amount):
        # your code here
        print(self.balance)
        self.balance = amount
        withdrawal_amt = int(input("amount to withdraw from account: "))
        if withdrawal_amt > self.balance:
            print("amount is invalid, Please try again.")
        amount = amount - withdrawal_amt
        return self
    def display_account_info(self):
        # your code here
        print(f"account balance: {self.balance}")
        return self
    def yield_interest(self):
        # your code here
        self.int_rate = rates
        self.balance = total
        interest_Rates = rates * total
        total = interest_Rates + total
        return self

Num882612 = BankAccount(int(input("Enter interest rates: ")), int(input("Inital dollar amount: ")))
Num554821 = BankAccount(int(input("Enter interest rates: ")), int(input("Inital dollar amount: ")))
Num554821.display_account_info().deposit()
Num882612.display_account_info().deposit()
Num882612.withdraw().display_account_info()
Num554821.withdraw().display_account_info()