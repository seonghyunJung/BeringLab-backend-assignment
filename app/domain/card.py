from abc import ABC, abstractmethod


class CardState(ABC):
    @abstractmethod
    async def enable(self, card):
        pass

    @abstractmethod
    async def disable(self, card):
        pass


class EnabledCardState(CardState):
    async def enable(self, card):
        print("The card is already enabled")

    async def disable(self, card):
        card.disable()
        return DisabledCardState()


class DisabledCardState(CardState):
    def enable(self, card):
        card.enable()
        return EnabledCardState()

    def disable(self, card):
        print("The card is already disabled")


class AccountCard:
    def __init__(self, card):
        self.card = card
        self.state = EnabledCardState()

    def enable(self):
        self.state.enable(self.card)
        self.state = EnabledCardState()

    def disable(self):
        self.state.disable(self.card)
        self.state = DisabledCardState()
