from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base


Base = declarative_base()


class Account(Base):
    __tablename__ = "account"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    phone_number = Column(String, nullable=False)
    balance = Column(Integer, default=0)

    cards = relationship("Card", back_populates="account")


class Card(Base):
    __tablename__ = "card"

    id = Column(Integer, primary_key=True)
    enabled = Column(Boolean, default=True)

    account_id = Column(Integer, ForeignKey("account.id"))
    account = relationship("Account", back_populates="cards")
