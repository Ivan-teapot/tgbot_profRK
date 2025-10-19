import asyncio
import os
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

load_dotenv()

BOT = os.getenv("BOT_TOKEN")
bot = Bot(token=os.getenv("BOT_TOKEN"))
dp = Dispatcher(bot)


@dp.message_handler(command=["start"])
async def start_handler(message):
    await message.answer("Бот запущен!")


async def main():
    print("Bot_started")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
