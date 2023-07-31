from aiogram import types
from aiogram.dispatcher import FSMContext

from State.Pharmacologenetics import Pharmacologenetics
from keyboards.inline import inline_menu_start


async def cmd_start(message: types.Message, state: FSMContext):
    await message.answer('Добро пожаловать в PharmacogeneticsBot!\nЯ помогу расшифровать результат анализа фармакогенетическое тестирование, давайте начнем.')
    kb = await inline_menu_start()
    await state.set_state(Pharmacologenetics.type.state)
    await message.answer('Было проведено выбранное фармакогенетическое тестирование:', reply_markup=kb)
