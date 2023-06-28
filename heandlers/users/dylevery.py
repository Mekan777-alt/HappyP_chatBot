from datetime import datetime
from aiogram.dispatcher import FSMContext
from aiogram.types import ChatActions
from buttons.users.dylevery import product_markup, categories_markup, menu_markup, category_cb, product_cb
from config import dp, db, bot
from aiogram import types


def time_dlv():
    current_time = str(datetime.now().time())
    return current_time


@dp.message_handler(text='🎒 Доставка')
async def cmd_dyl(message: types.Message):
    if time_dlv()[0] == '2' and time_dlv()[1] == '3' \
            or time_dlv()[0] == '0' \
            or time_dlv()[0] == '1' and time_dlv()[1] == '0':
        await message.answer("Доставка принимается с 11:00 до 23:00")
    else:
        db.query("INSERT INTO regime VALUES (?, ?)", (0, 1))
        is_allowed = db.fetchall('SELECT * FROM regime')
        if is_allowed[0][1] == 1:
            await message.answer("Минимальная сумма заказа 1000 рублей", reply_markup=menu_markup())
            await message.answer("ВЫБЕРИТЕ РАЗДЕЛ", reply_markup=categories_markup())
        else:
            await message.answer("Приносим извинения, на данный момент доставка не доступна")


@dp.message_handler(text='📖 МЕНЮ')
async def menu_dyl(message: types.Message):
    await message.answer("Выберите раздел", reply_markup=categories_markup())


@dp.message_handler(text="⚙️ Инструкция")
async def instruction(message: types.Message):
    pass


@dp.message_handler(text="💳 Способ оплаты")
async def pay(message: types.Message):
    pass


@dp.callback_query_handler(category_cb.filter(action='view_2'))
async def menu_dyl(call: types.CallbackQuery, callback_data: dict):
    products = db.fetchall('''SELECT * FROM products
        WHERE products.tag = (SELECT title FROM categories WHERE idx=?)''',
                           (callback_data['id'],))
    status = db.fetchall("SELECT * FROM status")
    await show_products(call.message, products, status)


@dp.callback_query_handler(product_cb.filter(action='add'))
async def add_product_callback_handler(query: types.CallbackQuery, callback_data: dict, state: FSMContext):
    product_id = callback_data['id']
    db.query('INSERT INTO cart VALUES (?, ?, 1, null, null, null, null, null)',
            (query.message.chat.id, product_id))
    await query.answer('Товар добавлен в корзину!')
    await query.message.delete()


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


