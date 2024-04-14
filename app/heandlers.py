from aiogram import Router, F, Bot
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

import os
import datetime
from work_to_subscribers import list_to_text_file, text_file_to_list

import app.keyboards as kb

router = Router()
bot = Bot(token='6702330987:AAFJXigFOLcZG-rXoKwPuGCOnNZ36glf6uc')

search_filter = {}


@router.message(F.text == '/start')
async def step1_1(message: Message):
    await message.answer('Старт работы бота:', reply_markup=kb.step1)


@router.callback_query(lambda callback_query: callback_query.data.startswith('schedule'))
async def step_1_2(callback: CallbackQuery, bot):
    await callback.message.answer(f'Выберите группу.')
    await bot.send_message(chat_id=callback.from_user.id, text='Выберите группу.', reply_markup=kb.groups_1)


@router.callback_query(lambda callback_query: callback_query.data.startswith('group_sod'))
async def step_1_2(callback: CallbackQuery, bot):
    await callback.message.answer(f'Выберите группу.')
    await bot.send_message(chat_id=callback.from_user.id,
                           text='СОД23-1: http://94.72.18.202:8083/raspisanie/www/cg59.htm \n'
                                'СОД23-2К: http://94.72.18.202:8083/raspisanie/www/cg60.htm \n'
                                'СОД21-1: http://94.72.18.202:8083/raspisanie/www/cg61.htm \n'
                                'СОД21-2К: http://94.72.18.202:8083/raspisanie/www/cg62.htm \n'
                                'СОД22-1: http://94.72.18.202:8083/raspisanie/www/cg63.htm \n'
                                'СОД22-2К: http://94.72.18.202:8083/raspisanie/www/cg64.htm')


@router.callback_query(lambda callback_query: callback_query.data.startswith('group_s'))
async def step_1_2(callback: CallbackQuery, bot):
    await callback.message.answer(f'Выберите группу.')
    await bot.send_message(chat_id=callback.from_user.id,
                           text='С20-1: http://94.72.18.202:8083/raspisanie/www/cg65.htm \n'
                                'С20-2: http://94.72.18.202:8083/raspisanie/www/cg66.htm \n'
                                'С20-4К: http://94.72.18.202:8083/raspisanie/www/cg67.htm \n'
                                'С20УЗ: http://94.72.18.202:8083/raspisanie/www/cg68.htm \n'
                                'С21-1: http://94.72.18.202:8083/raspisanie/www/cg69.htm \n'
                                'С21-2: http://94.72.18.202:8083/raspisanie/www/cg70.htm \n'
                                'С21-3: http://94.72.18.202:8083/raspisanie/www/cg71.htm \n'
                                'С21-4К: http://94.72.18.202:8083/raspisanie/www/cg72.htm \n'
                                'С21УЗ: http://94.72.18.202:8083/raspisanie/www/cg73.htm \n'
                                'С22-1: http://94.72.18.202:8083/raspisanie/www/cg74.htm \n'
                                'С22-2: http://94.72.18.202:8083/raspisanie/www/cg75.htm \n'
                                'С22-3К: http://94.72.18.202:8083/raspisanie/www/cg76.htm \n'
                                'С22уз: http://94.72.18.202:8083/raspisanie/www/cg77.htm \n'
                                'С23-1: http://94.72.18.202:8083/raspisanie/www/cg78.htm \n'
                                'С23-2: http://94.72.18.202:8083/raspisanie/www/cg79.htm \n'
                                'С23-3К: http://94.72.18.202:8083/raspisanie/www/cg80.htm \n'
                                'С23УЗ: http://94.72.18.202:8083/raspisanie/www/cg81.htm \n'
                           )


@router.callback_query(lambda callback_query: callback_query.data.startswith('group_umd'))
async def step_1_2(callback: CallbackQuery, bot):
    await callback.message.answer(f'Выберите группу.')
    await bot.send_message(chat_id=callback.from_user.id,
                           text='УМД 21-1: http://94.72.18.202:8083/raspisanie/www/cg82.htm \n'
                                'УМД 22-1: http://94.72.18.202:8083/raspisanie/www/cg83.htm \n'
                                'УМД23-1: http://94.72.18.202:8083/raspisanie/www/cg84.htm \n'
                           )


@router.callback_query(lambda callback_query: callback_query.data.startswith('group_sa'))
async def step_1_2(callback: CallbackQuery, bot):
    await callback.message.answer(f'Выберите группу.')
    await bot.send_message(chat_id=callback.from_user.id,
                           text='СА20-1: http://94.72.18.202:8083/raspisanie/www/cg85.htm \n'
                                'СА20-2К: http://94.72.18.202:8083/raspisanie/www/cg86.htm \n'
                                'СА21-1: http://94.72.18.202:8083/raspisanie/www/cg87.htm \n'
                                'СА21-2К: http://94.72.18.202:8083/raspisanie/www/cg88.htm \n'
                                'СА22-1: http://94.72.18.202:8083/raspisanie/www/cg89.htm \n'
                                'СА22-2: http://94.72.18.202:8083/raspisanie/www/cg90.htm \n'
                                'СА23-1: http://94.72.18.202:8083/raspisanie/www/cg91.htm \n'
                                'СА23-2: http://94.72.18.202:8083/raspisanie/www/cg92.htm \n'
                           )


@router.callback_query(lambda callback_query: callback_query.data.startswith('group_is'))
async def step_1_2(callback: CallbackQuery, bot):
    await callback.message.answer(f'Выберите группу.')
    await bot.send_message(chat_id=callback.from_user.id,
                           text='ИСа 22-1: http://94.72.18.202:8083/raspisanie/www/cg93.htm \n'
                                'ИСа23-1: http://94.72.18.202:8083/raspisanie/www/cg94.htm \n'
                                'ИСп 21-1: http://94.72.18.202:8083/raspisanie/www/cg95.htm \n'
                                'ИСп 21-2К: http://94.72.18.202:8083/raspisanie/www/cg96.htm \n'
                                'ИСп 22-1: http://94.72.18.202:8083/raspisanie/www/cg97.htm \n'
                                'ИСп20-1: http://94.72.18.202:8083/raspisanie/www/cg98.htm \n'
                                'ИСп20-2К: http://94.72.18.202:8083/raspisanie/www/cg99.htm \n'
                                'ИСп20-3К: http://94.72.18.202:8083/raspisanie/www/cg100.htm \n'
                                'ИСп20-4К: http://94.72.18.202:8083/raspisanie/www/cg101.htm \n'
                                'ИСп23-1: http://94.72.18.202:8083/raspisanie/www/cg102.htm \n'
                                'ИСп23-2К: http://94.72.18.202:8083/raspisanie/www/cg103.htm \n'
                                'ИСр 21-1: http://94.72.18.202:8083/raspisanie/www/cg104.htm \n'
                                'ИСр 21-2К: http://94.72.18.202:8083/raspisanie/www/cg105.htm \n'
                                'ИСр 22-1: http://94.72.18.202:8083/raspisanie/www/cg106.htm \n'
                                'ИСр23-1: http://94.72.18.202:8083/raspisanie/www/cg107.htm \n'
                                'ИСс 22-1: http://94.72.18.202:8083/raspisanie/www/cg108.htm \n'
                           )


@router.callback_query(lambda callback_query: callback_query.data.startswith('group_sv'))
async def step_1_2(callback: CallbackQuery, bot):
    await callback.message.answer(f'Выберите группу.')
    await bot.send_message(chat_id=callback.from_user.id,
                           text='СВ21-1К: http://94.72.18.202:8083/raspisanie/www/cg109.htm \n'
                                'СВ22-1К: http://94.72.18.202:8083/raspisanie/www/cg110.htm \n'
                                'СВ23-1: http://94.72.18.202:8083/raspisanie/www/cg111.htm \n'
                                'СВ23-2К: http://94.72.18.202:8083/raspisanie/www/cg112.htm \n'
                           )


@router.callback_query(lambda callback_query: callback_query.data.startswith('group_m'))
async def step_1_2(callback: CallbackQuery, bot):
    await callback.message.answer(f'Выберите группу.')
    await bot.send_message(chat_id=callback.from_user.id,
                           text='М21-1: http://94.72.18.202:8083/raspisanie/www/cg113.htm \n'
                                'М21-2К: http://94.72.18.202:8083/raspisanie/www/cg114.htm \n'
                                'М22-1: http://94.72.18.202:8083/raspisanie/www/cg115.htm \n'
                                'М23-1: http://94.72.18.202:8083/raspisanie/www/cg116.htm \n'
                           )


# @router.callback_query(lambda callback_query: callback_query.data.startswith('mailing'))
# async def subs_check(callback: CallbackQuery, bot):
#     user_id = callback.from_user.id
#
#     subscribers_list = await text_file_to_list()
#
#     if user_id in subscribers_list:
#         await callback.message.answer(f'Вы уже подписаны на рассылку!')
#         await bot.send_message(chat_id=callback.from_user.id, text='Выберите группу.', reply_markup=kb.step1)
#     else:
#         subscribers_list.append(user_id)
#         await list_to_text_file(subscribers_list)
#         await callback.message.answer(f'Вы успешно подписались на рассылку!')
#         await bot.send_message(chat_id=callback.from_user.id, text='Выберите группу.', reply_markup=kb.step1)


# def make_row_keyboard(items: list[str]) -> ReplyKeyboardMarkup:
#     row = [KeyboardButton(text=item) for item in items]
#     return ReplyKeyboardMarkup(keyboard=[row], resize_keyboard=True)


class Quantity(StatesGroup):
    five = State()
    fore = State()
    three = State()
    two = State()


@router.callback_query(lambda callback_query: callback_query.data.startswith('calk'))
async def calculation_rating(message: Message, state: FSMContext):
    await state.set_state(Quantity.five)
    await message.answer("Введите количество 5:")
    await message.answer("Введите количество 5:")


@router.message(Quantity.five)
async def quantity_five(message: Message, state: FSMContext):
    await state.update_data(five=message.text)
    await state.set_state(Quantity.fore)
    await message.answer("Введите количество 4:")


@router.message(Quantity.fore)
async def quantity_five(message: Message, state: FSMContext):
    await state.update_data(fore=message.text)
    await state.set_state(Quantity.three)
    await message.answer("Введите количество 3:")


@router.message(Quantity.three)
async def quantity_five(message: Message, state: FSMContext):
    await state.update_data(three=message.text)
    await state.set_state(Quantity.two)
    await message.answer("Введите количество 2:")


@router.message(Quantity.two)
async def quantity_five(message: Message, state: FSMContext):
    await state.update_data(two=message.text)

    data = await state.get_data()
    five, fore, three, two = int(data['five']), int(data['fore']), int(data['three']), int(data['two'])
    average_rating = ((five * 5) + (fore * 4) + (three * 3) + (two * 2)) / (five + fore + three + two)
    print(average_rating)

