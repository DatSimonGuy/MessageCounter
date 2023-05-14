import os
from dotenv import load_dotenv
import telethon
import telebot

load_dotenv()

BOT_TOKEN = os.environ.get('BOT_TOKEN')

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start', 'hello'])

def send_welcome(message):
    bot.reply_to(message, "Nya~")

chat = -1001153386748

bot.infinity_polling()