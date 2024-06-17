import telebot
import requests
#Это код бота-шутника, написанный catfy, бот англоязычный
TOKEN = 'Токен'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Hello! I'm a joke bot. To receive jokes, enter the /joke command.I'm written for a portfolio on kwork. ")

@bot.message_handler(commands=['joke'])
def joke(message):
    response = requests.get('https://official-joke-api.appspot.com/jokes/random/')
    joke_data = response.json()
    setup = joke_data['setup']
    punchline = joke_data['punchline']
    bot.reply_to(message, f"{setup}\n{punchline}")

bot.polling()







