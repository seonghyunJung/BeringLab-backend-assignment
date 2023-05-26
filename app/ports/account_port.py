from abc import ABC, abstractmethod


class AccountPort(ABC):
    @abstractmethod
    def create_account(self, name, phone_number):
        pass

    @abstractmethod
    def deposit(self, account, amount):
        pass

    @abstractmethod
    def withdraw(self, account, amount):
        pass

    @abstractmethod
    def get_balance(self, account):
        pass
