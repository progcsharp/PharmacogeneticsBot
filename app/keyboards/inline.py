from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def inline_menu_start():
    kb = InlineKeyboardMarkup(row_width=1)
    buttons = [InlineKeyboardButton(text='💊ИПП', callback_data='0'), InlineKeyboardButton(text='💊Клопидогрел', callback_data='1')]
    return kb.add(*buttons)


async def inline_menu_first_parameter():
    kb = InlineKeyboardMarkup(row_width=1)
    buttons = [
        InlineKeyboardButton(text='Гомозигота ТТ', callback_data="GTT"),
        InlineKeyboardButton(text='Гетерозигота СТ', callback_data="GetCT"),
        InlineKeyboardButton(text='Гомозигота CC', callback_data="GCC"),
        InlineKeyboardButton(text='Гомозигота CТ', callback_data="GCT"),
        InlineKeyboardButton(text='Гетерозигота ТТ', callback_data="GetTT"),
        InlineKeyboardButton(text='⬅️Назад', callback_data="back:1")
    ]
    return kb.add(*buttons)


async def inline_menu_second_parameter():
    kb = InlineKeyboardMarkup(row_width=1)
    buttons = [
        InlineKeyboardButton(text='Гомозигота GG', callback_data="GGG"),
        InlineKeyboardButton(text='Гомозигота AA', callback_data="GAA"),
        InlineKeyboardButton(text='Гетерозигота GA', callback_data="GetGA"),
        InlineKeyboardButton(text='⬅️Назад', callback_data="back:2")
    ]
    return kb.add(*buttons)


async def inline_menu_third_parameter():
    kb = InlineKeyboardMarkup(row_width=1)
    buttons = [
        InlineKeyboardButton(text='Гомозигота GG', callback_data="GGG"),
        InlineKeyboardButton(text='⬅️Назад', callback_data="back:3")
    ]
    return kb.add(*buttons)


async def inline_menu_fourth_parameter():
    kb = InlineKeyboardMarkup(row_width=1)
    buttons = [
        InlineKeyboardButton(text='Гетерозигота CT', callback_data="GetCT"),
        InlineKeyboardButton(text='Гомозигота CC', callback_data="GCC"),
        InlineKeyboardButton(text='Гомозигота TT', callback_data="GTT"),
        InlineKeyboardButton(text='⬅️Назад', callback_data="back:4")
    ]
    return kb.add(*buttons)


async def inline_menu_allele():
    kb = InlineKeyboardMarkup(row_width=1)
    buttons = [
        InlineKeyboardButton(text='*1/*17', callback_data="1"),
        InlineKeyboardButton(text='*2/*2', callback_data="2"),
        InlineKeyboardButton(text='*17/*17', callback_data="3"),
        InlineKeyboardButton(text='*1/*2', callback_data="4"),
        InlineKeyboardButton(text='*2/*17', callback_data="5"),
        InlineKeyboardButton(text='*1/*1', callback_data="6"),
        InlineKeyboardButton(text='⬅️Назад', callback_data="back:5")
    ]
    return kb.add(*buttons)


async def inline_menu_repeat():
    kb = InlineKeyboardMarkup(row_width=1)
    buttons = [InlineKeyboardButton(text='Повторить', callback_data="repeat")]
    return kb.add(*buttons)
