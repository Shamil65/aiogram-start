from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
import keyboards as kb

user = Router()




# Мы создаем его над функцией @user.message(), так у функции @user.message() нет фильтра 
# и он будет отбрабатыватиь все сообщения
@user.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Добро пожаловать в бот!',
                         reply_markup=kb.menu)


@user.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer('Вы написали команду /help')


@user.message(F.photo)
async def cmd_photo(message: Message):
    await message.answer(f'Вы скинули фото\n\nЕго id: {message.photo[-1].file_id}')
    await message.answer_photo(photo=message.photo[-2].file_id)


@user.message(F.text == 'Каталог')
async def cmd_hello(message: Message):
    await message.answer("Приветик молодой мальчик",
                         reply_markup=kb.catalog)


@user.message() # обрабатываем все сообщения
async def echo(message: Message):   # импортируем типы сообщений
    await message.send_copy(chat_id=message.from_user.id) # вернуть отправителю тоже самое
