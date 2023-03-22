from aiogram.dispatcher.filters.state import StatesGroup, State


class ReservedState(StatesGroup):
    name = State()
    time = State()
    date = State()
    people = State()
    phone_number = State()


class SosState(StatesGroup):
    question = State()
    phone_number = State()
    submit = State()


class Admin(StatesGroup):
    login = State()
    password = State()
