from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData


product_cb = CallbackData('product', 'id', 'action')


def product_markup(idx='', price=0):
    markup = InlineKeyboardMarkup()
    markup.add(
        InlineKeyboardButton(f'Заказать за - {price}₽', callback_data=product_cb.new(id=idx, action='add')))
    return markup
