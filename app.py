import asyncio
import logging
from datetime import datetime
from buttons.users.main import main
from config import dp, db, loop, bot
import heandlers
import aioschedule
from aiogram import executor, types
from aiogram.dispatcher import FSMContext


@dp.message_handler(commands='start', state="*")
async def start(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer('ДОБРО ПОЖАЛОВАТЬ, {0.first_name}\n'
                         'Я Ваш личный бот, помощник.\n'
                         'Я помогу Вам ознакомиться с меню, режимом работы ресторана и '
                         'забронировать стол.'.format(
        message.from_user), reply_markup=main())


async def send_message():
    current_date = datetime.utcnow().date()
    users = db.fetchall("SELECT * FROM users")
    for user in users:
        date_of_birth = datetime.utcfromtimestamp(user[3] / 1000).date()
        if date_of_birth.month == current_date.month and date_of_birth.day == current_date.day:
            await bot.send_message(int(user[0]), text="Дорогой наш гость,\n\n"
                                                      "Поздравляем вас с днём рождения! 🎉 От всей души желаем вам "
                                                      "радости, счастья и невероятных моментов в этот особенный день.\n"
                                                      "\n"
                                                      "В честь вашего праздника, мы предоставляем вам эксклюзивную "
                                                      "10% скидку на наше разнообразное меню! Наслаждайтесь "
                                                      "изысканными блюдами и удивительными напитками, чтобы сделать "
                                                      "этот день ещё более вкусным.\n\n"
                                                      "И это не всё! Ресторан акцию ещё на три дня после "
                                                      "вашего дня рождения. Так что вы можете продолжать наслаждаться "
                                                      "нашим гостеприимством и в течение следующих трёх дней.\n\n"
                                                      "С наилучшими пожеланиями и горячими поздравлениями,\n\n"
                                                      "Happy People!")
            await bot.send_message(chat_id=5443287345, text=f"У данного пользователя {user[1]} {user[2]} сегодня др\n"
                                                            f"Номер телефона: {user[4]}")


async def scheduler():
    aioschedule.every().day.at("10:00").do(send_message)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)


async def on_startup(_):
    logging.basicConfig(level=logging.INFO)
    db.create_tables()
    asyncio.create_task(scheduler())


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=False, on_startup=on_startup, loop=loop)
