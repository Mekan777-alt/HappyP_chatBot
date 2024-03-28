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
    photo = open('/root/HappyP_chatBot/photoMenu/photo_2024-03-28_18-49-10.jpg', 'rb')
    photo1 = open('/root/HappyP_chatBot/photoMenu/photo_2024-03-28_18-49-13.jpg', 'rb')
    photo2 = open('/root/HappyP_chatBot/photoMenu/photo_2024-03-28_18-49-15.jpg', 'rb')
    await bot.send_photo(message.from_user.id, photo)
    await bot.send_chat_action(message.from_user.id, ChatActions.UPLOAD_PHOTO)
    await asyncio.sleep(1)
    await bot.send_photo(message.from_user.id, photo1)
    await bot.send_chat_action(message.from_user.id, ChatActions.UPLOAD_PHOTO)
    await asyncio.sleep(1)
    await bot.send_photo(message.from_user.id, photo2)


@dp.message_handler(text='🥗 Холодные/Горячие закуски')
async def biznes(message: types.Message):
    photo = open('/root/HappyP_chatBot/photoMenu/photo_2024-03-28_18-48-41.jpg', 'rb')
    await bot.send_chat_action(message.from_user.id, ChatActions.UPLOAD_PHOTO)
    await bot.send_photo(message.from_user.id, photo)


@dp.message_handler(text='🥘 Основное меню')
async def main_menu(message: types.Message):
    photo = open('/root/HappyP_chatBot/photoMenu/photo_2024-03-28_18-48-59.jpg', 'rb')
    photo1 = open('/root/HappyP_chatBot/photoMenu/photo_2024-03-28_18-49-02.jpg', 'rb')
    photo2 = open('/root/HappyP_chatBot/photoMenu/photo_2024-03-28_18-49-04.jpg', 'rb')
    await bot.send_photo(message.from_user.id, photo)
    await bot.send_chat_action(message.from_user.id, ChatActions.UPLOAD_PHOTO)
    await asyncio.sleep(1)
    await bot.send_photo(message.from_user.id, photo1)
    await bot.send_chat_action(message.from_user.id, ChatActions.UPLOAD_PHOTO)
    await asyncio.sleep(1)
    await bot.send_photo(message.from_user.id, photo2)


@dp.message_handler(text='🍕 Пицца/Хачапури/Десерты')
async def pizza_menu(message: types.Message):
    photo = open('/root/HappyP_chatBot/photoMenu/photo_2024-03-28_18-49-07.jpg', 'rb')
    await bot.send_chat_action(message.from_user.id, ChatActions.UPLOAD_PHOTO)
    await bot.send_photo(message.from_user.id, photo)


@dp.message_handler(text='🍾 Бар')
async def catalog_bar(message: types.Message):
    await message.answer("Выберите позицию", reply_markup=bar_menu())


@dp.message_handler(text="🍸 Алкогольные напитки")
async def catalog_baz(message: types.Message):
    photo1 = open("/root/HappyP_chatBot/photoMenu/msg577119024-236499.jpg", 'rb')
    photo2 = open("/root/HappyP_chatBot/photoMenu/msg577119024-236496.jpg", 'rb')
    photo3 = open("/root/HappyP_chatBot/photoMenu/msg577119024-236497.jpg", 'rb')
    photo4 = open("/root/HappyP_chatBot/photoMenu/msg577119024-236489.jpg", 'rb')
    await bot.send_photo(message.from_user.id, photo1)
    await bot.send_chat_action(message.from_user.id, ChatActions.UPLOAD_PHOTO)
    await asyncio.sleep(1)
    await bot.send_photo(message.from_user.id, photo2)
    await bot.send_chat_action(message.from_user.id, ChatActions.UPLOAD_PHOTO)
    await asyncio.sleep(1)
    await bot.send_photo(message.from_user.id, photo3)
    await bot.send_chat_action(message.from_user.id, ChatActions.UPLOAD_PHOTO)
    await asyncio.sleep(1)
    await bot.send_photo(message.from_user.id, photo4)


@dp.message_handler(text="☕ Безалкогольные напитки")
async def bez_menu(message: types.Message):
    photo1 = open("/root/HappyP_chatBot/photoMenu/msg577119024-236492.jpg", "rb")
    photo2 = open("/root/HappyP_chatBot/photoMenu/msg577119024-236493.jpg", "rb")
    await bot.send_chat_action(message.from_user.id, ChatActions.UPLOAD_PHOTO)
    await bot.send_photo(message.from_user.id, photo1)
    await bot.send_chat_action(message.from_user.id, ChatActions.UPLOAD_PHOTO)
    await asyncio.sleep(1)
    await bot.send_photo(message.from_user.id, photo2)


@dp.message_handler(text='👈 Назад')
async def back(message: types.Message):
    await message.answer('Переход на главное меню', reply_markup=main())
