from config import dp
from secret import login, password
from aiogram import types
from context.context import Admin


@dp.message_handler(commands='admin')
async def start_admin(message: types.Message):
    await Admin.login.set()
    await message.answer('Введите логин: ')


@dp.message_handler(text=login, state=Admin.login)
async def set_password(message: types.Message):
    if message.text in login:
        await Admin.next()
        await message.answer('Пароль: ')


@dp.message_handler(lambda message: message.text is not login)
async def restart_login(message: types.Message):
    await message.answer('Неверный логин, повторите')


@dp.message_handler(lambda message: message.text is not password)
async def restart_password(message: types.Message):
    await message.answer('Неверный пароль, повторите')
