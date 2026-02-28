# Echo Bot — Теория

Этот бот показывает базовую структуру Telegram-бота на **aiogram 3**.

## Основные элементы

### 1. Загрузка токена

```python
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
```

Токен бота хранится в `.env` файле и загружается через библиотеку **python-dotenv**.

Это безопаснее, чем хранить токен в коде.

---

### 2. Создание бота

```python
bot = Bot(token=BOT_TOKEN)
```

Объект `Bot` отвечает за связь с Telegram API.

---

### 3. Dispatcher

```python
dp = Dispatcher()
```

`Dispatcher` принимает сообщения от Telegram и передаёт их обработчикам.

---

### 4. Обработчик сообщений

```python
@dp.message()
async def echo(message: Message):
    await message.send_copy(chat_id=message.from_user.id)
```

`@dp.message()` — обработчик всех сообщений.

Функция `echo()` получает объект `Message` — сообщение пользователя.

Метод `send_copy()` отправляет пользователю копию сообщения.

---

### 5. Polling

```python
await dp.start_polling(bot)
```

Бот постоянно отправляет запросы в Telegram и проверяет новые сообщения.

Этот способ называется **Polling**.

---

### 6. Запуск программы

```python
asyncio.run(main())
```

Запускает асинхронный код бота.

aiogram работает на **async/await**.

---

## Что изучено

* Bot
* Dispatcher
* Message
* Handler
* Polling
* async/await
* .env файл
