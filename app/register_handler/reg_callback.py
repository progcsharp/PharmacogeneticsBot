from aiogram import Dispatcher

from State.Pharmacologenetics import Pharmacologenetics
from handler.callback import call_type, call_first, call_back, call_end, call_third, call_allele, call_second, call_repeat


async def register_handlers_callback(dp: Dispatcher):
    dp.register_callback_query_handler(call_back, lambda call: call.data.find("back:") != -1,
                                       state="*")
    dp.register_callback_query_handler(call_repeat, lambda call: call.data == "repeat",
                                       state="*")
    dp.register_callback_query_handler(call_type,
                                       state=Pharmacologenetics.type)
    dp.register_callback_query_handler(call_first,
                                       state=Pharmacologenetics.first_parameter)
    dp.register_callback_query_handler(call_second,
                                       state=Pharmacologenetics.second_parameter)
    dp.register_callback_query_handler(call_third,
                                       state=Pharmacologenetics.third_parameter)
    dp.register_callback_query_handler(call_allele,
                                       state=Pharmacologenetics.fourth_parameter)
    dp.register_callback_query_handler(call_end,
                                       state=Pharmacologenetics.allele)

