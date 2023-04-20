from gino import Gino
from aiogram import Dispatcher
from db_api.schemas.users import Users_model
from db_api.schemas.bonus import Bonus_model
from db_api.schemas.achievement import Achievement_model
from settings import DATABASE_STR, db


async def on_startup_db(dispatcher: Dispatcher) -> None:
    await db.set_bind(DATABASE_STR)
    await db.gino.create_all()
    print('PostgreSQL connected')


async def on_shutdown_db(dispatcher: Dispatcher) -> None:
    await db.pop_bind().close()
