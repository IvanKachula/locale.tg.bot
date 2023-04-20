from aiogram import executor
import handlers
from db_api.db_gino import on_shutdown_db, on_startup_db
from config import dp


async def on_startup(_):
    print('Bot ONLINE')


if __name__ == "__main__":
    executor.start_polling(
        dp, skip_updates=True, on_startup=(on_startup_db, on_startup), on_shutdown=on_shutdown_db
    )
