from config import dp
from aiogram import types
from buttons.users.inline.dylevery import category_markup, menu_markup


@dp.message_handler(text='🎒 Доставка')
async def cmd_dyl(message: types.Message):
    await message.answer("Минимальная сумма заказа 2000 рублей", reply_markup=menu_markup())
    await message.answer("Выберите раздел", reply_markup=category_markup())


@dp.message_handler(text='📖 МЕНЮ')
async def menu_dyl(message: types.Message):
    await message.answer("Выберите раздел", reply_markup=category_markup())


@dp.message_handler(text="⚙️ Инструкция")
async def instruction(message: types.Message):
    pass


@dp.message_handler(text="💳 Способ оплаты")
async def pay(message: types.Message):
    pass




