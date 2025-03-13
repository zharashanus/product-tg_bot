import telebot
from dotenv import load_dotenv
import os
load_dotenv()


TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def handle_start(message):
    user_name = message.from_user.first_name
    bot.reply_to(message,f'Привет {user_name}, я простой бот для того чтобы посмотреть как работает продакшн окружение')


