from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from dotenv import load_dotenv
import os

storage = MemoryStorage()

# Initialize bot and dispatcher
load_dotenv()
bot = Bot(token=os.getenv("BOT_API_KEY"))
dp = Dispatcher(bot, storage=storage)
print(dp, bot)
