from app.models import Card
from sqlalchemy import select


class CardRepository:
    def __init__(self, session):
        self.session = session

    async def register_card(self, account_id):
        card = Card(account_id=account_id)
        self.session.add(card)
        await self.session.commit()
        return card.id

    async def disable(self, card_id):
        card = self.session.execute(select(Card).where(Card.id == card_id))
        if card:
            card.disable()
            await self.session.commit()

    async def enable(self, card_id):
        card = self.session.execute(select(Card).where(Card.id == card_id))
        if card:
            card.enable()
            await self.session.commit()
