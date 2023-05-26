import asyncio

from app.adapters.account_repository import AccountRepository
from app.adapters.card_repository import CardRepository
from app.services.account_service import AccountService
from app.services.card_service import CardService
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.config import get_db_uri

# from app.domain.account import Account
from app.models import Account
from sqlalchemy.orm import declarative_base
from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine, AsyncSession, async_scoped_session


def main():
    aio_engine = create_async_engine(get_db_uri(), future=True)
    with aio_engine.connect() as conn:
        sf: sessionmaker = sessionmaker(conn, expire_on_commit=False, autoflush=False, class_=AsyncSession)
        scoped_session = async_scoped_session(session_factory=sf, scopefunc=asyncio.current_task)

    async def session(session_factory: async_scoped_session):
        s: AsyncSession = session_factory()

    Base = declarative_base()
    Base.metadata.create_all(aio_engine)
    account = Account(name="Ryan")
    print(account.id)
    # session.add(account)
    # session.commit()
    #
    # # Create repositories
    # account_repository = AccountRepository(session)
    # card_repository = CardRepository(session)
    #
    # # Create services
    # account_service = AccountService(account_repository)
    # card_service = CardService(card_repository)
    #
    # # Perform bank operations
    # # Example usage:
    # account = account_service.create_account("John Doe")
    # card = card_service.register_card(account, "1234567890")
    #
    # account_service.deposit(account, 1000)
    # account_service.withdraw(account, 500)
    #
    # card_service.disable_card(card)
    # card_service.enable_card(card)
    #
    # session.commit()
    # session.close()


if __name__ == "__main__":
    main()
