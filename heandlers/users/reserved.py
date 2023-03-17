from config import dp, bot, BRON_CHANNEL
from aiogram import types
from aiogram.dispatcher import FSMContext
from context.context import ReservedState
from buttons.users.main import main
from buttons.users.reserved import cancel_reserved, phone_number, people, time, date_day, done_or_cancel
from aiogram.types import ContentType


@dp.message_handler(text='📞 Забронировать', state=None)
async def reserved_start(message: types.Message):
    await ReservedState.name.set()
    await message.answer('👤 На чье имя бронируем стол?', reply_markup=cancel_reserved())


@dp.message_handler(state=ReservedState.name)
async def set_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if message.text != "❌ Отменить":
            data['name'] = message.text
            await ReservedState.next()
            await message.answer('📅 На какую дату?', reply_markup=date_day())
        else:
            await state.finish()
            await message.answer("Переход на главное меню", reply_markup=main())


@dp.message_handler(state=ReservedState.date)
async def set_date(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['date'] = message.text
        await ReservedState.next()
        await message.answer('🕗 Выберите время бронирования: ', reply_markup=time())


@dp.message_handler(state=ReservedState.time)
async def set_time(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['time'] = message.text
        await ReservedState.next()
        await message.answer('👪 На какое количество гостей?', reply_markup=people())


@dp.message_handler(state=ReservedState.people)
async def set_people(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['people'] = message.text
        await ReservedState.next()
        await message.answer('Введите номер телефона пожалуйста.\n'
                             'Хостес перезвонит Вам для подтверждения брони.', reply_markup=phone_number())


@dp.message_handler(content_types=ContentType.CONTACT, state=ReservedState.phone_number)
async def set_phnumber_contact(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if message.contact is not None:
            data['phone_number'] = message.contact["phone_number"]
            await ReservedState.next()
            await message.answer(f"Отлично!\n"
                                 f"Будем ждать, {data['time']} в {data['people']}\n"
                                 f"на имя {data['name']}", reply_markup=done_or_cancel())


@dp.message_handler(state=ReservedState.phone_number)
async def set_phnumber(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['phone_number'] = message.text
        await ReservedState.next()
        await message.answer(f"Отлично!\n"
                             f"Будем ждать, {data['time']} в {data['people']}\n"
                             f"на имя {data['name']}", reply_markup=done_or_cancel())


@dp.message_handler(text="✅ Верно")
async def set_done(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        await bot.send_message(BRON_CHANNEL, f"Бронь\n"
                                             f"Ф.И.О: {data['name']}\n"
                                             f"Время: {data['people']}\n"
                                             f"Дата: {data['time']}\n"
                                             f"Кол-во гостей: {data['date']}\n"
                                             f"Номер телефона: {data['phone_number']}")
        await message.reply("Бронь принята\n"
                            "Ожидайте подтверждения", reply_markup=main())
    await state.finish()


@dp.message_handler(text="❌ Нет")
async def set_cancel(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, "Бронь отменена", reply_markup=main())
    await state.finish()
