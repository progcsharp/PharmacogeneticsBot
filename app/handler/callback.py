from aiogram import types
from aiogram.dispatcher import FSMContext

from State.Pharmacologenetics import Pharmacologenetics
from db.handlers.get import get_message
from handler.commands import cmd_start
from keyboards.inline import inline_menu_first_parameter, inline_menu_second_parameter, inline_menu_third_parameter, \
    inline_menu_fourth_parameter, inline_menu_allele, inline_menu_repeat, inline_menu_start


async def call_type(callback: types.CallbackQuery, state: FSMContext):
    await callback.answer()
    await callback.message.delete()
    async with state.proxy() as data:
        if callback.data.find("back:") == -1:
            if int(callback.data):
                data['type'] = True
            else:
                data['type'] = False
            await state.set_state(Pharmacologenetics.first_parameter)

    kb = await inline_menu_first_parameter()

    await callback.message.answer("Укажите первый параметр <b>ABCB1 C3433T</b>", reply_markup=kb)


async def call_first(callback: types.CallbackQuery, state: FSMContext):
    await callback.answer()
    await callback.message.delete()
    kb = await inline_menu_second_parameter()
    async with state.proxy() as data:
        if callback.data.find("back:") == -1:
            data["first_parameter"] = callback.data

    await state.set_state(Pharmacologenetics.second_parameter)

    await callback.message.answer("Укажите второй параметр <b>CYP2C19*2</b>", reply_markup=kb)


async def call_second(callback: types.CallbackQuery, state: FSMContext):
    await callback.answer()
    await callback.message.delete()
    kb = await inline_menu_third_parameter()
    async with state.proxy() as data:
        if callback.data.find("back:") == -1:
            data["second_parameter"] = callback.data

    await state.set_state(Pharmacologenetics.third_parameter)

    await callback.message.answer("Укажите третий параметр <b>CYP2C19*3</b>", reply_markup=kb)


async def call_third(callback: types.CallbackQuery, state: FSMContext):
    await callback.answer()
    await callback.message.delete()
    kb = await inline_menu_fourth_parameter()
    async with state.proxy() as data:
        if callback.data.find("back:") == -1:
            data["third_parameter"] = callback.data

    await state.set_state(Pharmacologenetics.fourth_parameter)

    await callback.message.answer("Укажите четвертый параметр <b>CYP2C19*17</b>", reply_markup=kb)


async def call_allele(callback: types.CallbackQuery, state: FSMContext):
    await callback.answer()
    await callback.message.delete()
    kb = await inline_menu_allele()
    async with state.proxy() as data:
        if callback.data.find("back:") == -1:
            data["fourth_parameter"] = callback.data

    await state.set_state(Pharmacologenetics.allele)

    await callback.message.answer("Укажите <b>CYP2C19 Аллель</b>", reply_markup=kb)


async def call_end(callback: types.CallbackQuery, state: FSMContext):
    await callback.answer()
    await callback.message.delete()

    async with state.proxy() as data:
        data["allele"] = callback.data
        message = await get_message(data)
        print(data)

    await state.finish()

    kb = await inline_menu_repeat()

    if message is None:
        message = "Извините, такой комбинации нет!"

    await callback.message.answer(message, reply_markup=kb)


async def call_repeat(callback: types.CallbackQuery, state: FSMContext):
    await callback.answer()

    await state.set_state(Pharmacologenetics.type.state)
    kb = await inline_menu_start()
    await callback.message.answer('Выберите какое фармакогенетическое тестирование было проведено:')
    await callback.message.answer('Было проведено выбранное фармакогенетическое тестирование:', reply_markup=kb)


async def call_back(callback: types.CallbackQuery, state: FSMContext):
    await callback.answer()
    back = callback.data.replace("back:", "")
    if int(back) == 1:
        await callback.message.delete()
        await state.set_state(Pharmacologenetics.type)
        await call_repeat(callback, state)
    elif int(back) == 2:
        await state.set_state(Pharmacologenetics.first_parameter)
        await call_type(callback, state)
    elif int(back) == 3:
        await state.set_state(Pharmacologenetics.second_parameter)
        await call_first(callback, state)
    elif int(back) == 4:
        await state.set_state(Pharmacologenetics.third_parameter)
        await call_second(callback, state)
    elif int(back) == 5:
        await state.set_state(Pharmacologenetics.fourth_parameter)
        await call_third(callback, state)
    print(back)
    # state_back.get(int(back), "svdsvs")
