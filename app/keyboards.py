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
    [InlineKeyboardButton(text='Назад в главное меню', callback_data='back_to_menu')]
])

back_to_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Назад в главное меню', callback_data='back_to_menu')]
])


# group_sod = InlineKeyboardMarkup(inline_keyboard=[
#     [InlineKeyboardButton(text='СОД23-1', callback_data= 'СОД23-1'),
#      InlineKeyboardButton(text='СОД23-2К', callback_data='СОД23-2К'),
#      InlineKeyboardButton(text='СОД21-1', callback_data= 'СОД21-1')],
#     [InlineKeyboardButton(text='СОД21-2К', callback_data='СОД21-2К'),
#      InlineKeyboardButton(text='СОД22-1', callback_data= 'СОД22-1'),
#      InlineKeyboardButton(text='СОД22-2К', callback_data='СОД22-2К')],
# ])
#
# group_s = InlineKeyboardMarkup(inline_keyboard=[
#     [InlineKeyboardButton(text='С20-1', callback_data='quantity_1_4'),
#      InlineKeyboardButton(text='С20-2', callback_data='quantity_2_4'),
#      InlineKeyboardButton(text='С20-4К', callback_data='quantity_3_4')],
#     [InlineKeyboardButton(text='С20УЗ', callback_data='quantity_4_4'),
#      InlineKeyboardButton(text='С21-1', callback_data='quantity_5_4'),
#      InlineKeyboardButton(text='С21-2', callback_data='quantity_6_4')],
#     [InlineKeyboardButton(text='С21-3', callback_data='quantity_7_4'),
#      InlineKeyboardButton(text='С21-4К', callback_data='quantity_8_4'),
#      InlineKeyboardButton(text='С21УЗ', callback_data='quantity_9_4')],
#     [InlineKeyboardButton(text='С22-1', callback_data='quantity_0_4'),
#      InlineKeyboardButton(text='С22-2', callback_data='quantity_1_3'),
#      InlineKeyboardButton(text='С22-3К', callback_data='quantity_2_3')],
#     [InlineKeyboardButton(text='С22уз', callback_data='quantity_3_3'),
#      InlineKeyboardButton(text='С23-1', callback_data='quantity_4_3'),
#      InlineKeyboardButton(text='С23-2', callback_data='quantity_5_3')],
#     [InlineKeyboardButton(text='С23-3К', callback_data='quantity_6_3'),
#      InlineKeyboardButton(text='С23УЗ', callback_data='quantity_7_3')],
# ])
#
# group_umd = InlineKeyboardMarkup(inline_keyboard=[
#     [InlineKeyboardButton(text='УМД 21-1', callback_data='quantity_1_2'),
#      InlineKeyboardButton(text='УМД 22-1', callback_data='quantity_2_2'),
#      InlineKeyboardButton(text='УМД23-1:', callback_data='quantity_3_2')]
# ])
#
# group_sa = InlineKeyboardMarkup(inline_keyboard=[
#     [InlineKeyboardButton(text='СА20-1:', callback_data='quantity_1_4'),
#      InlineKeyboardButton(text='СА20-2К', callback_data='quantity_2_4'),
#      InlineKeyboardButton(text='СА21-1', callback_data='quantity_3_4')],
# ])
#
# group_is = InlineKeyboardMarkup(inline_keyboard=[
#     [InlineKeyboardButton(text='ИСа 22-1', callback_data='quantity_1_4'),
#      InlineKeyboardButton(text='ИСа23-1', callback_data='quantity_2_4'),
#      InlineKeyboardButton(text='ИСп 21-1', callback_data='quantity_3_4')],
#     [InlineKeyboardButton(text='ИСп 21-2К', callback_data='quantity_4_4'),
#      InlineKeyboardButton(text='ИСп 22-1', callback_data='quantity_5_4'),
#      InlineKeyboardButton(text='ИСп20-1', callback_data='quantity_6_4')],
#     [InlineKeyboardButton(text='ИСп20-2К', callback_data='quantity_7_4'),
#      InlineKeyboardButton(text='ИСп20-3К', callback_data='quantity_8_4'),
#      InlineKeyboardButton(text='ИСп20-4К', callback_data='quantity_9_4')],
#     [InlineKeyboardButton(text='ИСп23-1', callback_data='quantity_0_4'),
#      InlineKeyboardButton(text='ИСп23-2К', callback_data='quantity_1_3'),
#      InlineKeyboardButton(text='ИСр 21-1', callback_data='quantity_2_3')],
#     [InlineKeyboardButton(text='ИСр 21-2К', callback_data='quantity_3_3'),
#      InlineKeyboardButton(text='ИСр 22-1', callback_data='quantity_4_3'),
#      InlineKeyboardButton(text='ИСр23-1', callback_data='quantity_5_3')],
#     [InlineKeyboardButton(text='ИСс 22-1', callback_data='quantity_6_3')]
# ])
#
# group_sv = InlineKeyboardMarkup(inline_keyboard=[
#     [InlineKeyboardButton(text='СВ21-1', callback_data='quantity_1_4'),
#      InlineKeyboardButton(text='СВ22-1', callback_data='quantity_2_4')],
#     [InlineKeyboardButton(text='СВ23-1', callback_data='quantity_3_4'),
#      InlineKeyboardButton(text='СВ23-2', callback_data='quantity_3_4')],
# ])
#
# group_m = InlineKeyboardMarkup(inline_keyboard=[
#     [InlineKeyboardButton(text='М21-1', callback_data='quantity_1_4'),
#      InlineKeyboardButton(text='М21-2К', callback_data='quantity_2_4')],
#     [InlineKeyboardButton(text='М22-1', callback_data='quantity_3_4'),
#      InlineKeyboardButton(text='М23-1', callback_data='quantity_3_4')],
# ])