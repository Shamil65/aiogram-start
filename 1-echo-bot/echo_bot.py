from aiogram import Bot, Dispatcher, F
from dotenv import load_dotenv
import os
from handlers import user


load_dotenv()              # Обработка updates/управляет входящими и исходящими сообщениями
BOT_TOKEN = os.getenv("BOT_TOKEN")

async def main():
    bot = Bot(token=BOT_TOKEN)      # Подкоючение к нашему боту
    dp = Dispatcher()  
    dp.include_router(user)
    await dp.start_polling(bot)     # Обращение к polling/ будет постоянно посылать запрос 
                                    # в телеграм и справшивать, а пришло ли какое то обновление


if __name__ == "__main__":
    try:
        import asyncio
        asyncio.run(main())
    except:
        pass
