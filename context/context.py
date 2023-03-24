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


class ProductState(StatesGroup):
    title = State()
    body = State()
    image = State()
    price = State()
    confirm = State()


class CategoryState(StatesGroup):
    title = State()