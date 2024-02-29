from aiogram import types
from aiogram.dispatcher import FSMContext

from buttons.users.main import main
from context.context import LoyalRegister
from config import dp, db, generate_number
from buttons.users.carta_loyal import loyal_markup, carta_loyal


@dp.message_handler(text='💳 Карта лояльности')
async def start_loyal(message: types.Message):
    check_user = db.fetchone("SELECT id FROM users WHERE id = ?", (message.from_user.id,))
    if not check_user:
        await message.answer("Описание карты лояльности!", reply_markup=loyal_markup())
    else:
        await message.answer("Описание карты лояльности!", reply_markup=carta_loyal())


@dp.message_handler(text="💳 Виртуальная карта")
async def virt_cart(message: types.Message):
    cart_number = db.fetchone("SELECT entry_number FROM users WHERE id = ?", (message.from_user.id,))
    await message.answer(f"<b>Продиктуйте данный код менеджеру ресторана</b> \n(вместе с дефисом, он важен)\n"
                         f"\n"
                         f"<b>{cart_number[0]}</b>", parse_mode="HTML")


@dp.message_handler(text="👛Баланс")
async def sum_money_user(message: types.Message):
    balance = db.fetchone("SELECT balance FROM users WHERE id = ?", (message.from_user.id,))
    await message.answer(f"Баланс вашего счета состовляет <b>{balance[0]} руб</b>", parse_mode="HTML")


@dp.message_handler(text="👤 Зарегистрироваться")
async def register_user(message: types.Message, state: FSMContext):
    await message.answer("Введите ваше имя")
    await state.set_state(LoyalRegister.name)


@dp.message_handler(state=LoyalRegister.name)
async def register_user(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
        await message.answer("Введите вашу фамилию", reply_markup=types.ReplyKeyboardRemove())
        await state.set_state(LoyalRegister.lastname)


@dp.message_handler(state=LoyalRegister.lastname)
async def register_lastname(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['lastname'] = message.text
        await message.answer("Введите телефон номер:\n"
                             "\n"
                             "В таком формате (89123456789)")
        await state.set_state(LoyalRegister.phone_number)


@dp.message_handler(state=LoyalRegister.phone_number)
async def register_birthday(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['phone_number'] = message.text
        await message.answer("Введите дату рождения в формате дд.мм.гггг \n"
                             "(Например: 31.01.1999).")
        await state.set_state(LoyalRegister.birthday)


@dp.message_handler(state=LoyalRegister.birthday)
async def register_phone_number(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['birthday'] = message.text
        entry_number = await generate_number()
        db.query(
            f"INSERT INTO users (id, name, lastname, birthday, phone_number, entry_number, balance) VALUES (?, ?, ?, ?, ?, ?, ?)",
            (message.from_user.id, data['name'], data['lastname'], data['birthday'],
             data['phone_number'], entry_number, 0.0))
        await message.answer("Принято", reply_markup=main())
        await state.finish()


@dp.message_handler(text="🔙 Назад")
async def register_back(message: types.Message):
    await message.answer("Главное меню", reply_markup=main())
