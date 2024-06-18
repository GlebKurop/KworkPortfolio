import requests
from bs4 import BeautifulSoup
import telebot
from telebot import types

token = '6465392718:AAH3wMYGQQ2LtPO1dQaRZHSAw_yj0kxkgPI'


bot = telebot.TeleBot(token)
#Команда /start
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет! Я погодный бот, у меня в наличии 3 Украинских города, напиши команду /weather и выбери город, что-бы узнать погоду')

 #Погода в Киеве
def weather_parse_Kiev():
    url_Kiev = 'https://meteoscope.net/ua/weather/kyiv-182847?param=ads_search&gad_source=1&gclid=Cj0KCQjw4MSzBhC8ARIsAPFOuyX0Upj-NKOaTYTe_7fPxd_VVtTVg5Ee_4M4Z4D_MbsRUU_v-Ys26sgaAp9dEALw_wcB'
    r = requests.get(url_Kiev)
    soup = BeautifulSoup(r.text, 'html.parser')
    weather_Kiev = soup.find('p', class_='weather-description').text.strip()
    temperature = soup.find('p', class_='current-temperature').text.strip()
    time = soup.find('span', class_='current-time').text.strip()
    return weather_Kiev, temperature, time
# Погода в Днепре
def weather_parse_Dnipro():
    url_Dnipro = "https://meteoscope.net/ua/weather/dnipro-18770"
    r = requests.get(url_Dnipro)
    soup = BeautifulSoup(r.text, 'html.parser')
    weather_Dnipro = soup.find('p', class_='weather-description').text.strip()
    temperature_Dnipro = soup.find('p', class_='current-temperature').text.strip()
    time1 = soup.find('span', class_='current-time').text.strip()
    return weather_Dnipro, temperature_Dnipro, time1
#Погода в Полтаве
def weather_parse_Poltava():
    url_Poltava = "https://meteoscope.net/ua/weather/poltava-28110"
    r = requests.get(url_Poltava)
    soup = BeautifulSoup(r.text, 'html.parser')
    weather_Poltava = soup.find('p', class_='weather-description').text.strip()
    temperature_Poltava = soup.find('p', class_='current-temperature').text.strip()
    time2 = soup.find('span', class_='current-time').text.strip()
    return weather_Poltava, temperature_Poltava, time2
@bot.message_handler(commands=['weather'])
def weather(message):
    markup = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
    btn1 = types.KeyboardButton('Киев')
    btn2 = types.KeyboardButton('Днепр')
    btn3 = types.KeyboardButton('Полтава')
    markup.add(btn1, btn2, btn3)
    bot.send_message(message.chat.id, "Выберите город:", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text in ['Киев', 'Днепр', 'Полтава'])
def send_weather(message):
    city = message.text
    if city == 'Киев':
        weather_Kiev, temperature, time = weather_parse_Kiev()
        bot.send_message(message.chat.id, f'Погода в Киеве: Время на момент вычислений⌚: {time}, Погода🌧: {weather_Kiev}, Температура🌡: {temperature} ')
    elif city == 'Днепр':
        weather_Dnipro, temperature_Dnipro, time1 = weather_parse_Dnipro()
        bot.send_message(message.chat.id, f'Погода в Днепре: Время на момент вычислений⌚: {time1}, Погода🌧: {weather_Dnipro}, Температура🌡: {temperature_Dnipro}')
    elif city == 'Полтава':
        weather_Poltava, temperature_Poltava, time2 = weather_parse_Poltava()
        bot.send_message(message.chat.id, f'Погода в Полтаве: Время на момент вычислений⌚: {time2}, Погода🌧: {weather_Poltava}, Температура🌡: {temperature_Poltava}')

weather_parse_Kiev()
weather_parse_Dnipro()
weather_parse_Poltava()

bot.polling()