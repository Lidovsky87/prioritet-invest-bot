import logging
import os
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = os.getenv("ADMIN_ID")

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

LANGUAGES = {"uk": "🇺🇦 Українська", "en": "🇬🇧 English", "ru": "🇷🇺 Русский"}
user_lang = {}

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for code, label in LANGUAGES.items():
        kb.add(types.KeyboardButton(label))
    await message.answer("Оберіть мову / Choose language / Выберите язык:", reply_markup=kb)

@dp.message_handler(lambda message: message.text in LANGUAGES.values())
async def set_language(message: types.Message):
    lang_code = [k for k, v in LANGUAGES.items() if v == message.text][0]
    user_lang[message.from_user.id] = lang_code
    greetings = {
        "uk": "Вітаємо у Prioritet Invest! Тут з’являтимуться аналітичні сигнали та попередження.",
        "en": "Welcome to Prioritet Invest! Here you'll receive analytical signals and alerts.",
        "ru": "Добро пожаловать в Prioritet Invest! Здесь будут сигналы и аналитика."
    }
    await message.answer(greetings[lang_code])

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
