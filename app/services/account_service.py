from app.ports.account_port import AccountPort


class AccountService(AccountPort):
    def __init__(self, account_repository):
        self.account_repository = account_repository

    def create_account(self, name, phone_number):
        account = self.account_repository.create_account(name, phone_number)
        return account

    def deposit(self, account_id, amount):
        self.account_repository.deposit(account_id, amount)

    def withdraw(self, account_id, amount):
        self.account_repository.withdraw(account_id, amount)

    def get_balance(self, account_id):
        return self.account_repository.get_balance(account_id)
