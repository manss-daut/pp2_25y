class Bank_Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def deposit(self, addAmount):
        self.balance += addAmount
        print(f"Deposit successful. New Balance: {self.balance}")
    def withdraw(self, takeAmount):
        if self.balance < takeAmount:
            print(f'There are currently insufficient funds. Your balance: {self.balance}')
        else: 
            self.balance -= takeAmount
            print(f"Withdraw successful. New Balance: {self.balance}")
bank_op = Bank_Account("Dautov Mansur", 100)
bank_op.deposit(50)
bank_op.withdraw(150)