from config import dp
from aiogram import types


@dp.message_handler(text='📖 Меню')
async def catalog_menu(message: types.Message):
    await message.answer('ссылка')


@dp.message_handler(text='🍾 Бар')
async def catalog_bar(message: types.Message):
    await message.answer('ссылка')
