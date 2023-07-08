import asyncio
import os
from aiogram import Dispatcher, Bot, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from data.database import Database

loop = asyncio.get_event_loop()
TOKEN = '6261279510:AAGW27LozQLygnhr2yzKrOXturXyr-r4Rcc'
TOKEN_PAYMENTS = "test_XBzEk_bjy4PkSe17lDz-Z3jdfT7S89q31pzPhhx27Rw"
DELIVERY_CHAT = "-1001973443055"
SUPPORT_CHAT = ""
BRON_CHANNEL = "-1001921643359"

storage = MemoryStorage()

path = os.getcwd() + "/data/database.db"

try:
    from local_config import *
except ImportError:
    pass


bot = Bot(token=TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=storage, loop=loop)
db = Database(path)
