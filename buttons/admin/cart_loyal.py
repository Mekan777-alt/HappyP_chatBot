from aiogram.types import ReplyKeyboardMarkup


def loyal_markup_admin():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("Просмотреть пользователей")
    markup.add("Обновить баланс")
    return markup
