from aiogram import Bot, Dispatcher, F
from dotenv import load_dotenv
import os
from handlers import user

# Загружаем токен из .env
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

async def main():
    # Подключаемся к боту
    bot = Bot(token=BOT_TOKEN)
    
    # Создаем диспетчер
    dp = Dispatcher()
    
    # Подключаем обработчики из routers
    dp.include_router(user)
    
    # Запуск polling: бот постоянно проверяет новые сообщения
    await dp.start_polling(bot)

# Точка входа
if __name__ == "__main__":
    try:
        import asyncio
        asyncio.run(main())
    except:
        pass