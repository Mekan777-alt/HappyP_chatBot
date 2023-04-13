from aiogram.types import ChatActions

from buttons.users.dylevery import product_markup
from config import dp, db, bot
from aiogram import types
from buttons.users.inline.dylevery import category_markup, menu_markup, category_cb


@dp.message_handler(text='🎒 Доставка')
async def cmd_dyl(message: types.Message):
    await message.answer("Минимальная сумма заказа 2000 рублей", reply_markup=menu_markup())
    await message.answer("Выберите раздел", reply_markup=category_markup())


@dp.message_handler(text='📖 МЕНЮ')
async def menu_dyl(message: types.Message):
    await message.answer("Выберите раздел", reply_markup=category_markup())


@dp.message_handler(text="⚙️ Инструкция")
async def instruction(message: types.Message):
    pass


@dp.message_handler(text="💳 Способ оплаты")
async def pay(message: types.Message):
    pass


async def show_products(m, products, status):
    if len(products) == 0:
        await m.answer('Здесь ничего нет 😢')

        await bot.send_chat_action(m.chat.id, ChatActions.TYPING)
    else:
        for idx, title, body, image, price, _ in products:
            for id, stat in status:
                if idx in id and stat in 'start':
                    markup = product_markup(idx, price)
                    text = f'<b>{title}</b>\n\n{body}'
                    if image:
                        await m.answer_photo(photo=image,
                                             caption=text,
                                             reply_markup=markup)
                    else:
                        await m.answer(text=text, reply_markup=markup)


@dp.callback_query_handler(category_cb.filter(action='view_2'))
async def menu_dyl(call: types.CallbackQuery, callback_data: dict):
    products = db.fetchall('''SELECT * FROM products
        WHERE products.tag = (SELECT title FROM categories WHERE idx=?)''',
                           (callback_data['id'],))
    status = db.fetchall("SELECT * FROM status")
    await show_products(call.message, products, status)
