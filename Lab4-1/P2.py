class BankAccount:
    saving_run = 0
    loan_run = 0
    branch_number = 5511
    
    def __init__(self, name, acc_type='saving', balance=0): # constructor
        self.name = name
        self.type = acc_type
        self.balance = balance
        
        if self.type == 'saving':
            BankAccount.saving_run += 1
            self.runing = f"{BankAccount.branch_number}-1-{BankAccount.saving_run}"
        else:
            BankAccount.loan_run += 1
            self.runing = f"{BankAccount.branch_number}-2-{BankAccount.loan_run}"
    
    def deposit(self, amount):
        self.balance += amount
    
    def get_balance(self):
        return self.balance
    
    def withdraw(self, amount):
        self.balance -= amount

    def print_customer(self):
        print("----- Customer Record -----")
        print(f"Name: {self.name}")
        print(f"Account number: {self.runing}")
        print(f"Account type: {self.type}")
        print(f"Balance: {self.balance:,}")
        print("----- End Record -----")

john = BankAccount("John", "saving", 500)
tim = BankAccount("Tim", "loan", -1000000)
sarah = BankAccount("Sarah", "saving")

# John deposit 3,000 and check balance
john.deposit(3000)
print(f"John balance: {john.get_balance():,}\n")

# Tim check loan and pay half of the balance
print(f"Tim loan: {tim.get_balance():,}")
tim.withdraw((tim.get_balance()) / 2)
print(f"After payment: {tim.get_balance():,}\n")

# Sarah deposit 50,000,000
sarah.deposit(50000000)

# Sarah open loan account
sarah_loan = BankAccount("Sarah", "loan", -100000000)

# show print_customer
john.print_customer()
print()
tim.print_customer()
print()
sarah.print_customer()
print()
sarah_loan.print_customer()