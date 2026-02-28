from aiogram import F, Router
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext
from aiogram.filters import CommandStart, Command
import keyboards as kb
from states import Reg

user = Router()




# Мы создаем его над функцией @user.message(), так у функции @user.message() нет фильтра 
# и он будет отбрабатыватиь все сообщения
@user.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    await message.answer('Добро пожаловать в бот!\nВведите ваше имя',
                         reply_markup=ReplyKeyboardRemove())
    await state.set_state(Reg.name)


@user.message(Reg.name)
async def reg_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer('Отправьте номер телефона',
                         reply_markup=kb.get_number)
    await state.set_state(Reg.phone)





@user.message(Reg.phone, F.contact)
async def reg_contact(message: Message, state: FSMContext):
    await state.update_data(phone=message.contact.phone_number)

    data = await state.get_data()
    await message.answer(f'Вы успешно зарегистрировались\nИмя:{data["name"]}, Номер телефона {data["phone"]}',
                         reply_markup=kb.menu)
    await state.clear()


@user.message(Reg.phone)
async def reg_contact2(message: Message):
    await message.answer('Отправьте контакты по кнопке ниже')


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


@user.callback_query(F.data.startswith('brand_'))
async def check_brand(callback: CallbackQuery):
    brand_name = callback.data.split('_')[1]
    await callback.answer(f'Вы выбрали {brand_name.capitalize()}', show_alert=True)
    await callback.message.answer(f'Вы выбрали {brand_name.capitalize()}!')


@user.message() # обрабатываем все сообщения
async def echo(message: Message):   # импортируем типы сообщений
    await message.send_copy(chat_id=message.from_user.id) # вернуть отправителю тоже самое
