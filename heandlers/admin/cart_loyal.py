from aiogram.dispatcher import FSMContext

from buttons.admin.admin import admin
from context.context import UpdateBalance
from config import db, dp
from buttons.admin.cart_loyal import loyal_markup_admin
from aiogram import types


@dp.message_handler(text="Обновить баланс пользователя по карте лояльности")
async def admin_cart_loyal(message: types.Message):
    await message.answer("Выберите команду", reply_markup=loyal_markup_admin())


@dp.message_handler(text="Просмотреть пользователей")
async def admin_cart_users(message: types.Message):
    users = db.fetchall("SELECT * FROM users")
    if users:
        text = ""
        for user in users:
            user = (f"ФИО: {user[2]} {user[1]}\n"
                    f"Телефон номер: {user[3]}\n"
                    f"Баланс: {user[4]} руб\n"
                    f"__________________________\n")
            text += user
        await message.answer(text, reply_markup=loyal_markup_admin())
    else:
        await message.answer("Cписок пуст!", reply_markup=loyal_markup_admin())


@dp.message_handler(text="Обновить баланс")
async def update_balance(message: types.Message, state: FSMContext):
    await message.answer("Введите телефон номер пользователя")
    await state.set_state(UpdateBalance.phone)


@dp.message_handler(state=UpdateBalance.phone)
async def set_number(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["phone"] = message.text
        await message.answer("Введите счет")
        await state.set_state(UpdateBalance.money)


@dp.message_handler(state=UpdateBalance.money)
async def set_money(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["money"] = message.text
        balance_user = int(data["money"])
        phone_number = data["phone"]
        db.query("UPDATE users SET balance = balance + ? WHERE phone_number = ?", (balance_user, phone_number))
        await message.answer("Принято!", reply_markup=admin())
        await state.finish()
