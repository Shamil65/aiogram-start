from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
import os
import asyncio
from aiogram.types import Message

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)      # Подкоючение к нашему боту
dp = Dispatcher()               # Обработка updates/управляет входящими и исходящими сообщениями


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
