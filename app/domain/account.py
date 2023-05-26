class BankAccount:
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            raise ValueError("Insufficient funds")

    def check_balance(self):
        return self.balance
