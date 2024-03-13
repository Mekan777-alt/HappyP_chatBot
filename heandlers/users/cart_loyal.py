from datetime import datetime

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
        await message.answer("Добро пожаловать в мир удовольствий и выгод! Рады представить вам нашу карту лояльности "
                             "– волшебный билет в мир вкуса и привилегий. При регистрации в нашем ресторане вы "
                             "получаете не только незабываемый опыт гастрономических открытий, но и привилегии на "
                             "каждом шагу.\n\n"
                             "🌟 Преимущества нашей карты лояльности: \n\n"
                             "5% скидки по регистрации на депозит от 5000 руб ..Далее как ваша цель достигает 40000 руб ,"
                             " ваши скидка на депозит от 5000 руб будет составлять 10%\n\n"
                             "Эксклюзивные предложения. Будьте в курсе наших специальных предложений и акций, "
                             "доступных исключительно обладателям карты лояльности. Первыми узнавайте о новых блюдах, "
                             "мероприятиях и ужинах под открытым небом.\n\n"
                             "Персонализированный сервис. Мы заботимся о каждом госте. Карта лояльности позволяет нам "
                             "предоставлять вам индивидуальные предложения и подходить к вашему опыту обслуживания с "
                             "особым вниманием.\n\n"
                             "Присоединяйтесь к нашему клубу лояльности и дарите себе моменты удовольствия, а нам – "
                             "возможность делиться с вами лучшим из того, что у нас есть. Ждем вас в нашем ресторане! "
                             "🍽", reply_markup=loyal_markup())
    else:
        await message.answer("Выберите раздел", reply_markup=carta_loyal())


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
        date_obj = datetime.strptime(message.text, "%d.%m.%Y")
        entry_number = await generate_number()
        db.query(
            f"INSERT INTO users (id, name, lastname, birthday, phone_number, entry_number, balance) VALUES (?, ?, ?, ?, ?, ?, ?)",
            (message.from_user.id, data['name'], data['lastname'], date_obj,
             data['phone_number'], entry_number, 0.0))
        await message.answer("Принято", reply_markup=main())
        await state.finish()


@dp.message_handler(text="🔙 Назад")
async def register_back(message: types.Message):
    await message.answer("Главное меню", reply_markup=main())
