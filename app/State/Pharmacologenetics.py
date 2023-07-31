from aiogram.dispatcher.filters.state import StatesGroup, State


class Pharmacologenetics(StatesGroup):
    type = State()
    first_parameter = State()
    second_parameter = State()
    third_parameter = State()
    fourth_parameter = State()
    allele = State()
