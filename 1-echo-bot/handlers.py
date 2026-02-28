from aiogram import F, Router
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext
from aiogram.filters import CommandStart, Command
import keyboards as kb
from states import Reg

# Создаем Router для группы обработчиков
user = Router()

# Команда /start — начало регистрации
@user.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    await message.answer(
        'Добро пожаловать в бот!\nВведите ваше имя',
        reply_markup=ReplyKeyboardRemove()  # Скрываем клавиатуру
    )
    await state.set_state(Reg.name)  # Ставим состояние ожидания имени

# Состояние: ввод имени
@user.message(Reg.name)
async def reg_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)  # Сохраняем имя
    await message.answer(
        'Отправьте номер телефона',
        reply_markup=kb.get_number  # Кнопка "Отправить номер"
    )
    await state.set_state(Reg.phone)  # Переходим к состоянию телефона

# Состояние: контакт пользователя
@user.message(Reg.phone, F.contact)
async def reg_contact(message: Message, state: FSMContext):
    await state.update_data(phone=message.contact.phone_number)  # Сохраняем номер
    data = await state.get_data()
    await message.answer(
        f'Вы успешно зарегистрировались\nИмя: {data["name"]}, Номер телефона: {data["phone"]}',
        reply_markup=kb.menu
    )
    await state.clear()  # Сбрасываем состояние

# Если пользователь прислал текст вместо контакта
@user.message(Reg.phone)
async def reg_contact2(message: Message):
    await message.answer('Отправьте контакты по кнопке ниже')

# Команда /help
@user.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer('Вы написали команду /help')

# Обработка фото
@user.message(F.photo)
async def cmd_photo(message: Message):
    await message.answer(f'Вы скинули фото\n\nЕго id: {message.photo[-1].file_id}')
    await message.answer_photo(photo=message.photo[-2].file_id)

# Кнопка "Каталог"
@user.message(F.text == 'Каталог')
async def cmd_hello(message: Message):
    await message.answer(
        "Приветик молодой мальчик",
        reply_markup=kb.catalog
    )

# Callback кнопки брендов
@user.callback_query(F.data.startswith('brand_'))
async def check_brand(callback: CallbackQuery):
    brand_name = callback.data.split('_')[1]
    await callback.answer(f'Вы выбрали {brand_name.capitalize()}', show_alert=True)
    await callback.message.answer(f'Вы выбрали {brand_name.capitalize()}!')

# Эхо для всех остальных сообщений
@user.message()
async def echo(message: Message):
    await message.send_copy(chat_id=message.from_user.id)