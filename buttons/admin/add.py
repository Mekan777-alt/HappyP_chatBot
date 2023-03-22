from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

regime_cb = CallbackData('regime_2', 'id', 'action')


def regime_start(idx):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("▶ Старт", regime_cb.new(id=idx, action='start')))
    return markup


def regime_stop(idx):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("⏸ Стоп", regime_cb.new(id=idx, action='stop')))
    return markup

