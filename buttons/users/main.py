from aiogram.types import ReplyKeyboardMarkup


def main():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('📖 Меню', '🍾 Бар', '📞 Забронировать')
    markup.add('🕗 Режим работы', '🎒 Доставка', '? Помощь')
    return markup

