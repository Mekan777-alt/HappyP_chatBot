from aiogram.types import ReplyKeyboardMarkup


def loyal_markup():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("👤 Зарегистрироваться")
    markup.add("🔙 Назад")
    return markup