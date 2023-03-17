import logging
from config import dp, db, loop
import hendlers
from aiogram import executor


async def on_startup(dp):
    logging.basicConfig(level=logging.INFO)
    db.create_tables()


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=False, on_startup=on_startup, loop=loop)
