from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton, 
                          InlineKeyboardMarkup, InlineKeyboardButton)

menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Каталог')],
        [KeyboardButton(text='Корзина'), KeyboardButton(text='Контакты')],
    ],
    resize_keyboard=True,
    input_field_placeholder='Выберите пункт меню'
)

catalog = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Nike', url='https://translate.yandex.ru/')],
        [InlineKeyboardButton(text='Adidas', url='https://translate.yandex.ru/')],
        [InlineKeyboardButton(text='Reebok', url='https://translate.yandex.ru/')],
    ]
)