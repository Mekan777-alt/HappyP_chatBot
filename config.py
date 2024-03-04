import asyncio
import os
import random

from aiogram import Dispatcher, Bot, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from data.database import Database
from dotenv import load_dotenv

load_dotenv()

loop = asyncio.get_event_loop()
TOKEN = os.getenv("TOKEN")
TOKEN_PAYMENTS = os.getenv("TOKEN_PAYMENTS")
DELIVERY_CHAT = os.getenv("DELIVERY_CHAT")
SUPPORT_CHAT = os.getenv("SOS_CHAT")
BRON_CHANNEL = os.getenv("BRON_CHANNEL")

storage = MemoryStorage()

path = os.getcwd() + "/database.sqlite"

try:
    from local_config import *
except ImportError:
    pass


bot = Bot(token=TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=storage, loop=loop)
db = Database(path)


async def generate_number():

    unique_digits = random.sample(range(0, 10), 6)

    digits_string = "".join(map(str, unique_digits))

    result_string = '-'.join(digits_string[i:i+3] for i in range(0, len(digits_string), 3))

    return result_string
