from config import dp
from aiogram import types
from buttons.users.menu import menu
from buttons.users.main import main


@dp.message_handler(text='📖 Меню')
async def catalog_menu(message: types.Message):
    await message.answer('Что вас интересует?', reply_markup=menu())


@dp.message_handler(text='🍳 Завтраки')
async def dinner(message: types.Message):
    await message.answer('По ссылке ниже можете ознакомиться с Завтраками\n'
                         '\n'
                         'https://qr.vsem-edu-oblako.ru/?merchantKey=6a3bcb79dff2b98025e610d7a01bdf7e#/catalog/10086110')


@dp.message_handler(text='🥪 Бизнес ланч')
async def biznes(message: types.Message):
    await message.answer('По ссылке ниже можете ознакомиться с Бизнес-ланчами\n'
                         '\n'
                         'https://qr.vsem-edu-oblako.ru/?merchantKey=6a3bcb79dff2b98025e610d7a01bdf7e#/catalog/10089026')


@dp.message_handler(text='📓 Основное меню')
async def main_menu(message: types.Message):
    await message.answer('По ссылке ниже можете ознакомиться с Основным меню\n'
                         '\n'
                         'https://qr.vsem-edu-oblako.ru/?merchantKey=6a3bcb79dff2b98025e610d7a01bdf7e#/catalog/10085742')


@dp.message_handler(text='🍾 Бар')
async def catalog_bar(message: types.Message):
    await message.answer('С баром можете ознакомиться с ссылкой ниже\n'
                         'https://qr.vsem-edu-oblako.ru/?merchantKey=6a3bcb79dff2b98025e610d7a01bdf7e#/catalog/10085743'
                         )


@dp.message_handler(text='👈 Назад')
async def back(message: types.Message):
    await message.answer('Переход на главное меню', reply_markup=main())
