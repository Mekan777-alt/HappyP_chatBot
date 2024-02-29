from aiogram.dispatcher import FSMContext
from buttons.admin.admin import admin
from context.context import UpdateBalance
from config import db, dp
from buttons.admin.cart_loyal import loyal_markup_admin, back_menu
from aiogram import types


@dp.message_handler(text="Обновить баланс пользователя по карте лояльности")
async def admin_cart_loyal(message: types.Message):
    await message.answer("Выберите команду", reply_markup=loyal_markup_admin())


@dp.message_handler(text="Просмотреть пользователей")
async def admin_cart_users(message: types.Message):
    users = db.fetchall("SELECT * FROM users")
    print(users)
    if users:
        text = ""
        for user in users:
            user = (f"<b>ФИО: {user[2]} {user[1]}</b>\n"
                    f"<b>Телефон номер: {user[3]}</b>\n"
                    f"<b>Баланс: {user[6]} руб</b>\n"
                    f"<b>Код пополнения: {user[5]}</b>\n"
                    f"__________________________\n")
            text += user
        await message.answer(text, reply_markup=loyal_markup_admin(), parse_mode="HTML")
    else:
        await message.answer("Cписок пуст!", reply_markup=loyal_markup_admin())


@dp.message_handler(text="Обновить баланс")
async def update_balance(message: types.Message, state: FSMContext):
    await message.answer("Введите код пользователя", reply_markup=types.ReplyKeyboardRemove())
    await state.set_state(UpdateBalance.code)


@dp.message_handler(state=UpdateBalance.code)
async def set_number(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["code"] = message.text
        await message.answer("Введите счет", reply_markup=back_menu())
        await state.set_state(UpdateBalance.money)


@dp.message_handler(state=UpdateBalance.money)
async def set_money(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["money"] = message.text
        balance_user = int(data["money"])
        code = data["code"]
        db.query("UPDATE users SET balance = balance + ? WHERE entry_number = ?", (balance_user, code))
        await message.answer("Принято!", reply_markup=admin())
        await state.finish()
