# Echo & Command Bot — Теория

Мини-бот на Python с aiogram 3.  

## Основные элементы

- **Токен** хранится в `.env` и подключается через `python-dotenv`
- **Bot** — связь с Telegram API
- **Dispatcher** — обработка сообщений и команд

## Обработчики

- `/start` — приветствие пользователя
- `/help` — вывод информации
- Фото — бот отвечает id и пересылает фото
- Эхо — все остальные сообщения бот повторяет пользователю

## Запуск

Бот работает на **Polling** (`asyncio.run(dp.start_polling(bot))`)  
Использует **async/await**

## Изучено

- Команды и фильтры (`CommandStart`, `Command`, `F.photo`)  
- Эхо-сообщения  
- Асинхронный код  
- Работа с `.env` и токеном


## Пример работы с файлами

```python
@dp.message(F.sticker)
async def cmd_photo(message: Message):
    await message.answer(f'Вы скинули стикер\n\nЕго id: {message.sticker.file_id}')
    await message.answer_sticker(sticker=message.sticker.file_id)
```
