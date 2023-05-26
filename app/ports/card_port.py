from abc import ABC, abstractmethod


class CardPort(ABC):
    @abstractmethod
    def register_card(self, account_id):
        pass

    @abstractmethod
    def disable(self, card_id):
        pass

    @abstractmethod
    def enable(self, card_id):
        pass
