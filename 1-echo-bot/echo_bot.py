from aiogram import Bot, Dispatcher, F
from dotenv import load_dotenv
import os
import asyncio
from aiogram.types import Message
from aiogram.filters import CommandStart, Command

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)      # Подкоючение к нашему боту
dp = Dispatcher()               # Обработка updates/управляет входящими и исходящими сообщениями


# Мы создаем его над функцией @dp.message(), так у функции @dp.message() нет фильтра 
# и он будет отбрабатыватиь все сообщения
@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Добро пожаловать в бот!')


@dp.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer('Вы написали команду /help')


@dp.message(F.photo)
async def cmd_photo(message: Message):
    await message.answer(f'Вы скинули фото\n\nЕго id: {message.photo[-1].file_id}')
    await message.answer_photo(photo=message.photo[-2].file_id)



@dp.message() # обрабатываем все сообщения
async def echo(message: Message):   # импортируем типы сообщений
    await message.send_copy(chat_id=message.from_user.id) # вернуть отправителю тоже самое


async def main():
    await dp.start_polling(bot)     # Обращение к polling/ будет постоянно посылать запрос 
                                    # в телеграм и справшивать, а пришло ли какое то обновление


if __name__ == "__main__":
    try:
        import asyncio
        asyncio.run(main())
    except:
        pass
