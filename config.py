from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import Bot, Dispatcher
from language_middleware import setup_middleware


API_TOKEN = "TOKEN_HERE"


storage = MemoryStorage()


bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=storage)


i18n = setup_middleware(dp)
_ = i18n.gettext




