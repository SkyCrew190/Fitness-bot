import os
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

TOKEN = os.getenv("BOT_TOKEN")  # Токен бота из переменных окружения

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Привет! Я помогу тебе с планом питания и тренировок 💪")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
