from aiogram.dispatcher.filters.state import StatesGroup, State


class FSMreserved(StatesGroup):
    name = State()
    time = State()
    date = State()
    people = State()
    phone_number = State()


