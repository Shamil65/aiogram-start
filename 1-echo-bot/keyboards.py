from aiogram.types import (
    ReplyKeyboardMarkup, KeyboardButton,
    InlineKeyboardMarkup, InlineKeyboardButton
)

# Главное меню
menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Каталог')],
        [KeyboardButton(text='Корзина'), KeyboardButton(text='Контакты')],
    ],
    resize_keyboard=True,
    input_field_placeholder='Выберите пункт меню'
)

# Inline кнопки для каталога брендов
catalog = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Nike', callback_data='brand_nike')],
        [InlineKeyboardButton(text='Adidas', callback_data='brand_adidas')],
        [InlineKeyboardButton(text='Reebok', callback_data='brand_reebok')],
    ]
)

# Кнопка для отправки контакта
get_number = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Отправить номер', request_contact=True)]
    ]
)