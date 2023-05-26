import pytest
from faker import Faker
import asyncio

from app.adapters.account_repository import AccountRepository
from app.services.account_service import AccountService
from app.adapters.card_repository import CardRepository
from app.services.card_service import CardService
from sqlalchemy import select
from app.models import Account, Card

fake = Faker()


def account_factory(session, name, phone_number):
    account_service = AccountService(AccountRepository(session))
    account_id = account_service.create_account(name, phone_number)
    return account_id


def card_factory(session, account_id):
    card_service = CardService(CardRepository(session))
    card_id = card_service.register_card(account_id)
    return card_id


@pytest.mark.asyncio
async def test_create_user_account(session):
    name = fake.name()
    phone_number = fake.phone_number()
    account_id = account_factory(session, name, phone_number)
    temp = session.execute(select(Account).where(Account.name == name and Account.phone_number == phone_number))


@pytest.mark.asyncio
async def test_register_cards(session):
    name = fake.name()
    phone_number = fake.phone_number()
    account_id = account_factory(session, name, phone_number)
    card_id = card_factory(session, account_id)

    assert session.execute(select(Card).where(Card.account_id == account_id))


@pytest.mark.asyncio
async def test_disable_card(session):
    name = fake.name()
    phone_number = fake.phone_number()
    account_id = account_factory(session, name, phone_number)
    card_id = card_factory(session, account_id=account_id)

    card_service = CardService(CardRepository(session))
    card_service.disable(card_id)
    assert session.execute(select(Card.enabled).where(Card.id == card_id))


@pytest.mark.asyncio
async def test_enable_card(session):
    name = fake.name()
    phone_number = fake.phone_number()
    account_id = account_factory(session, name, phone_number)
    card_id = card_factory(session, account_id=account_id)

    card_service = CardService(CardRepository(session))
    card_service.enable(card_id)


@pytest.mark.asyncio
async def test_deposit_cash(session):
    name = fake.name()
    phone_number = fake.phone_number()
    account_id = account_factory(session, name, phone_number)

    account_service = AccountService(AccountRepository(session))
    account_service.deposit(account_id, 100)
    balance = session.execute(select(Account).where(Account.id == account_id))


@pytest.mark.asyncio
async def test_withdraw_cash(session):
    name = fake.name()
    phone_number = fake.phone_number()
    account_id = account_factory(session, name, phone_number)

    account_service = AccountService(AccountRepository(session))
    account_service.withdraw(account_id, 50)


@pytest.mark.asyncio
async def test_check_account_balance(session):
    name = fake.name()
    phone_number = fake.phone_number()
    account_id = account_factory(session, name, phone_number)
    card_id = card_factory(session, account_id=account_id)

    account_service = AccountService(AccountRepository(session))
    card_service = CardService(CardRepository(session))
    assert account_service.get_balance(account_id) == 0
    await account_service.deposit(account_id, 100)
    assert account_service.get_balance(account_id) == 100
    await account_service.withdraw(account_id, 50)
    assert account_service.get_balance(account_id) == 50
