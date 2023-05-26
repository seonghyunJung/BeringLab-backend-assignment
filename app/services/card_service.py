from app.ports.card_port import CardPort


class CardService(CardPort):
    def __init__(self, card_repository):
        self.card_repository = card_repository

    def register_card(self, account_id):
        return self.card_repository.register_card(account_id)

    def disable(self, card_id):
        self.card_repository.disable(card_id)

    def enable(self, card_id):
        self.card_repository.enable(card_id)
