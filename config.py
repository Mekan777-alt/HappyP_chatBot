import asyncio
import os
from aiogram import Dispatcher, Bot, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from data.database import Database

loop = asyncio.get_event_loop()
TOKEN = ""
TOKEN_PAYMENTS = ""
DELIVERY_CHAT = ""
SUPPORT_CHAT = ""
BRON_CHANNEL = ""

storage = MemoryStorage()

path = os.getcwd() + "/data/database.db"

try:
    from local_config import *
except ImportError:
    pass


bot = Bot(token=TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=storage, loop=loop)
db = Database(path)
