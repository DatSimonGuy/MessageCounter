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

names = []
messages = []


def Display():
    i = 0
    for name in names:
        print(name + f' {messages[i]}')
        i+=1

chat = int(os.environ.get('CHAT'))
api_id = os.environ.get('ID')
api_hash = os.environ.get('HASH')



from telethon.sync import TelegramClient

client = TelegramClient('session_id', api_id, api_hash)
n = 0
with client:
    for msg in client.iter_messages(chat, 100000):
        n+=1
        print(n)
        if n%10000 == 0:
            Display()
        if msg.sender.first_name in names:
            messages[names.index(msg.sender.first_name)] += 1


bot.infinity_polling()