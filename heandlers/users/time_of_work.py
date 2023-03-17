from config import dp, bot
from aiogram import types


@dp.message_handler(text='🕗 Режим работы')
async def time_work(message: types.Message):
    await message.answer("Happy People\n"
                         "\n"
                         "Режим работы:\n"
                         "ПН-ВС\n"
                         "С 11:00 до 00:00\n"
                         "\n"
                         "Адрес: Мусина 1\n"
                         "\n"
                         "☎️ Тел:  +7 (843) 266-11-11\n")
    await bot.send_location(message.from_user.id, latitude=55.81693801144643, longitude=49.11948637935675)
