import asyncio

from config import dp, bot
from aiogram import types
from buttons.users.menu import menu, bar_menu
from buttons.users.main import main
from aiogram.types import ChatActions


@dp.message_handler(text='📖 Меню')
async def catalog_menu(message: types.Message):
    await message.answer('Что вас интересует?', reply_markup=menu())


@dp.message_handler(text='🍣 Авторские роллы от Шефа Суши')
async def dinner(message: types.Message):
    photo = open('../../photoMenu/msg577119024-236488.jpg', 'rb')
    photo1 = open('../../photoMenu/msg577119024-236487.jpg', 'rb')
    photo2 = open('../../photoMenu/msg577119024-236498.jpg', 'rb')
    await bot.send_chat_action(message.from_user.id, ChatActions.UPLOAD_PHOTO)
    await bot.send_photo(message.from_user.id, photo)
    await asyncio.sleep(1)
    await bot.send_photo(message.from_user, photo1)
    await asyncio.sleep(1)
    await bot.send_photo(message.from_user.id, photo2)


@dp.message_handler(text='🥗 Холодные закуски')
async def biznes(message: types.Message):
    photo = open('../../photoMenu/msg577119024-236495.jpg', 'rb')
    await bot.send_chat_action(message.from_user.id, ChatActions.UPLOAD_PHOTO)
    await bot.send_photo(message.from_user.id, photo)


@dp.message_handler(text='🥘 Основное меню')
async def main_menu(message: types.Message):
    photo = open('../../photoMenu/msg577119024-236485.jpg', 'rb')
    photo1 = open('../../photoMenu/msg577119024-236490.jpg', 'rb')
    photo2 = open('../../photoMenu/msg577119024-236494.jpg', 'rb')
    await bot.send_chat_action(message.from_user.id, ChatActions.UPLOAD_PHOTO)
    await bot.send_photo(message.from_user.id, photo)
    await asyncio.sleep(1)
    await bot.send_photo(message.from_user, photo1)
    await asyncio.sleep(1)
    await bot.send_photo(message.from_user.id, photo2)



@dp.message_handler(text='🍕 Выпечка/Пицца')
async def pizza_menu(message: types.Message):
    photo = open('../../photoMenu/msg577119024-236486.jpg', 'rb')
    await bot.send_chat_action(message.from_user.id, ChatActions.UPLOAD_PHOTO)
    await bot.send_photo(message.from_user.id, photo)

@dp.message_handler(text='🍾 Бар')
async def catalog_bar(message: types.Message):
    await message.answer("Выберите позицию", reply_markup=bar_menu())


@dp.message_handler(text="🍸 Алкогольные напитки")
async def catalog_baz(message: types.Message):
    photo1 = open("../../photoMenu/msg577119024-236499.jpg", 'rb')
    photo2 = open("../../photoMenu/msg577119024-236496.jpg", 'rb')
    photo3 = open("../../photoMenu/msg577119024-236497.jpg", 'rb')
    photo4 = open("../../photoMenu/msg577119024-236489.jpg", 'rb')
    await bot.send_chat_action(message.from_user.id, ChatActions.UPLOAD_PHOTO)
    await bot.send_photo(message.from_user.id, photo1)
    await asyncio.sleep(1)
    await bot.send_photo(message.from_user.id, photo2)
    await asyncio.sleep(1)
    await bot.send_photo(message.from_user.id, photo3)
    await asyncio.sleep(1)
    await bot.send_photo(message.from_user.id, photo4)


@dp.message_handler(text="☕ Безалкогольные напитки")
async def bez_menu(message: types.Message):
    photo1 = open("../../photoMenu/msg577119024-236492.jpg", "rb")
    photo2 = open("../../photoMenu/msg577119024-236493.jpg", "rb")
    await bot.send_chat_action(message.from_user.id, ChatActions.UPLOAD_PHOTO)
    await bot.send_photo(message.from_user.id, photo1)
    await asyncio.sleep(1)
    await bot.send_photo(message.from_user.id, photo2)


@dp.message_handler(text='👈 Назад')
async def back(message: types.Message):
    await message.answer('Переход на главное меню', reply_markup=main())
