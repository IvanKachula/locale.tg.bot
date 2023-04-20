from aiogram.contrib.fsm_storage.memory import MemoryStorage
from dotenv import load_dotenv
from pathlib import Path
from gino import Gino
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base


storage = MemoryStorage()


db = Gino()

I18N_DOMAIN = 'tg_bot'
BASE_DIR = Path(__file__).resolve().parent
LOCALES_DIR = BASE_DIR/'locales'
ENV_PATH = BASE_DIR.joinpath(".env")


load_dotenv(dotenv_path=ENV_PATH)



DATABASE = {
    "NAME": "NAME",
    "USER": "USER",
    "PASSWORD": "PASSWORD",
    "HOST": "HOST",
}

# База данных тип postgresql, mysql

DATABASE_TYPE = "postgresql"
DATABASE_STR = ""

if DATABASE_TYPE == "postgresql":
    DATABASE_STR = (
        f"postgresql://{DATABASE['USER']}:{DATABASE['PASSWORD']}"
        f"@{DATABASE['HOST']}/{DATABASE['NAME']}"
    )


engine = create_engine(f"postgresql+psycopg2://postgres:{DATABASE['PASSWORD']}@{DATABASE['HOST']}/{DATABASE['NAME']}")
session = scoped_session(sessionmaker(bind=engine))
Base = declarative_base()
Base.query = session.query_property()


DEFAULT_LOCALE = 'en'
UK_LOCALE = 'uk'
RU_LOCALE = 'ru'
