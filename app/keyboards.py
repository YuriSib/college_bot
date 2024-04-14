from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


quantity_5 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']


main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='/start')]
],
                           resize_keyboard=True,
                           input_field_placeholder='Выберите пункт ниже')


step1 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Расписание занятий', callback_data='schedule')],
    [InlineKeyboardButton(text='Рассылка новостей', callback_data='mailing')],
    [InlineKeyboardButton(text='Калькулятор успеваемости', callback_data='calk')],
    [InlineKeyboardButton(text='Дополнительные вопросы', callback_data='faq')],
])


groups_1 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='СОД', callback_data='group_sod'),
     InlineKeyboardButton(text='С', callback_data='group_s')],
    [InlineKeyboardButton(text='УМД', callback_data='group_umd'),
     InlineKeyboardButton(text='СА', callback_data='group_sa')],
    [InlineKeyboardButton(text='ИС', callback_data='group_is'),
     InlineKeyboardButton(text='СВ', callback_data='group_sv')],
    [InlineKeyboardButton(text='М', callback_data='group_m')],
])

quantity_5 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='1', callback_data='quantity_1_5'),
     InlineKeyboardButton(text='2', callback_data='quantity_2_5'),
     InlineKeyboardButton(text='3', callback_data='quantity_3_5')],
    [InlineKeyboardButton(text='4', callback_data='quantity_4_5'),
     InlineKeyboardButton(text='5', callback_data='quantity_5_5'),
     InlineKeyboardButton(text='6', callback_data='quantity_6_5')],
    [InlineKeyboardButton(text='7', callback_data='quantity_7_5'),
     InlineKeyboardButton(text='8', callback_data='quantity_8_5'),
     InlineKeyboardButton(text='9', callback_data='quantity_9_5')],
    [InlineKeyboardButton(text='0', callback_data='quantity_0_5')]
])

quantity_4 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='1', callback_data='quantity_1_4'),
     InlineKeyboardButton(text='2', callback_data='quantity_2_4'),
     InlineKeyboardButton(text='3', callback_data='quantity_3_4')],
    [InlineKeyboardButton(text='4', callback_data='quantity_4_4'),
     InlineKeyboardButton(text='5', callback_data='quantity_5_4'),
     InlineKeyboardButton(text='6', callback_data='quantity_6_4')],
    [InlineKeyboardButton(text='7', callback_data='quantity_7_4'),
     InlineKeyboardButton(text='8', callback_data='quantity_8_4'),
     InlineKeyboardButton(text='9', callback_data='quantity_9_4')],
    [InlineKeyboardButton(text='0', callback_data='quantity_0_4')]
])

quantity_3 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='1', callback_data='quantity_1_3'),
     InlineKeyboardButton(text='2', callback_data='quantity_2_3'),
     InlineKeyboardButton(text='3', callback_data='quantity_3_3')],
    [InlineKeyboardButton(text='4', callback_data='quantity_4_3'),
     InlineKeyboardButton(text='5', callback_data='quantity_5_3'),
     InlineKeyboardButton(text='6', callback_data='quantity_6_3')],
    [InlineKeyboardButton(text='7', callback_data='quantity_7_3'),
     InlineKeyboardButton(text='8', callback_data='quantity_8_3'),
     InlineKeyboardButton(text='9', callback_data='quantity_9_3')],
    [InlineKeyboardButton(text='0', callback_data='quantity_0_3')]
])

quantity_2 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='1', callback_data='quantity_1_2'),
     InlineKeyboardButton(text='2', callback_data='quantity_2_2'),
     InlineKeyboardButton(text='3', callback_data='quantity_3_2')],
    [InlineKeyboardButton(text='4', callback_data='quantity_4_2'),
     InlineKeyboardButton(text='5', callback_data='quantity_5_2'),
     InlineKeyboardButton(text='6', callback_data='quantity_6_2')],
    [InlineKeyboardButton(text='7', callback_data='quantity_7_2'),
     InlineKeyboardButton(text='8', callback_data='quantity_8_2'),
     InlineKeyboardButton(text='9', callback_data='quantity_9_2')],
    [InlineKeyboardButton(text='0', callback_data='quantity_0_2')]
])
