from aiogram import types
from aiogram.dispatcher import FSMContext

from buttons.users.main import main
from context.context import LoyalRegister
from config import dp, db
from buttons.users.carta_loyal import loyal_markup


@dp.message_handler(text='💳 Карта лояльности')
async def start_loyal(message: types.Message):
    await message.answer("Описание карты лояльности!", reply_markup=loyal_markup())


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
                             "В таком формате 89123456789")
        await state.set_state(LoyalRegister.phone_number)


@dp.message_handler(state=LoyalRegister.phone_number)
async def register_phone_number(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['phone_number'] = message.text
        db.query(f"INSERT INTO users (id, name, lastname, phone_number, balance) VALUES (?, ?, ?, ?, ?)",
                 (message.from_user.id, data['name'], data['lastname'], data['phone_number'], 0.0))
        await message.answer("Принято", reply_markup=main())
        await state.finish()


@dp.message_handler(text="🔙 Назад")
async def register_back(message: types.Message):
    await message.answer("Главное меню", reply_markup=main())
