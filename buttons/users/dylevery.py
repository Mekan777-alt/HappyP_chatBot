from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup
from aiogram.utils.callback_data import CallbackData
from config import db

product_cb = CallbackData('product', 'id', 'action')


def product_markup(idx='', price=0):
    markup = InlineKeyboardMarkup()
    markup.add(
        InlineKeyboardButton(f'Заказать за - {price}₽', callback_data=product_cb.new(id=idx, action='add')))
    return markup


category_cb = CallbackData('category', 'id', 'action')


def categories_markup():
    markup = InlineKeyboardMarkup()
    for idx, title in db.fetchall('SELECT * FROM categories'):
        markup.add(InlineKeyboardButton(title, callback_data=category_cb.new(id=idx, action='view_2')))

    return markup


def menu_markup():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('📖 МЕНЮ')
    markup.add("⚙️ Инструкция", "💳 Способ оплаты")
    markup.add('👈 Назад')
    markup.add('🛒 Перейти в Корзину')
    return markup
