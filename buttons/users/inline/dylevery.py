from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData
from config import db
from aiogram.types import ReplyKeyboardMarkup

category_cb = CallbackData('category', 'id', 'action')


def category_markup():
    markup = InlineKeyboardMarkup()
    for idx, title in db.fetchall('SELECT * FROM categories'):
        markup.add(InlineKeyboardButton(title, callback_data=category_cb.new(id=idx, action='view_2')))


def menu_markup():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('📖 МЕНЮ')
    markup.add("⚙️ Инструкция", "💳 Способ оплаты")
    return markup
