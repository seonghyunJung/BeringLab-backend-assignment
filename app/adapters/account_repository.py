from app.models import Account


class AccountRepository:
    def __init__(self, session):
        self.session = session

    async def create_account(self, name, phone_number):
        account = Account(name=name, phone_number=phone_number)
        await self.session.commit()
        return account.id

    async def deposit(self, account_id, amount):
        account = self.session.query(Account).get(account_id)
        if account:
            account.balance += amount
            await self.session.commit()

    async def withdraw(self, account_id, amount):
        account = self.session.query(Account).get(account_id)
        if account and account.balance >= amount:
            account.balance -= amount
            await self.session.commit()

    async def get_balance(self, account_id, amount):
        account = self.session.query(Account).get(account_id)
        if account and account.balance >= amount:
            account.balance -= amount
            await self.session.commit()
