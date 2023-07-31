from aiogram import Dispatcher


from handler.message import message_example


async def register_handlers_message(dp: Dispatcher):
    dp.register_message_handler(message_example)
