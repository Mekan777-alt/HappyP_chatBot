from aiogram.types import ReplyKeyboardMarkup


def menu():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('🍳 Завтраки', '🥪 Бизнес ланч')
    markup.add('📓 Основное меню')
    markup.add('👈 Назад')
    return markup


