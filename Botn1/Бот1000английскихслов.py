import csv
import random
import requests
from bs4 import BeautifulSoup
import telebot

token = '7069698490:AAGTZPYtVihQtm0g9bgvT4iNYlZ0LAdMZ74'

bot = telebot.TeleBot(token)

def parse_words():
    url = 'https://puzzle-english.com/directory/1000-popular-words'  # адрес сайта
    r = requests.get(url)  # отправляю запрос get на адрес сайта
    soup = BeautifulSoup(r.text, 'html.parser')

    words = [] # создаю лист words

    # ищу все элементы <li> со style "font-weight: 400;"  в которых и хранятся 1000 слов
    word_wrappers = soup.find_all('li', attrs={'style': 'font-weight: 400;'})


    for word_wrapper in word_wrappers:
        # Извлекаю текст слова
        word = word_wrapper.text.strip()
        words.append(word)

    if not words:
        print("Не удалось найти слова с указанным стилем.")

    return words

def save_to_csv(words, filename='words_with_translations.csv'):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(['Слово'])  # Заголовок столбца
        for word in words:
            csvwriter.writerow([word])

    print(f'Данные успешно сохранены в файл {filename}')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f'Привет, {message.from_user.username}! Я телеграмм бот который содержит в себе 1000 разных английских слов, напиши команду /newword и ты получаешь одно из 1000 английских слов с транскрипцией и переводом!')

@bot.message_handler(commands=['newword'])
def newword(message):
    # Генерируем случайный индекс для списка слов
    random_index = random.randint(0, len(words_list) - 1)
    random_word = words_list[random_index]
    bot.send_message(message.chat.id, f'Случайное слово: {random_word}')


words_list = parse_words()


# save_to_csv(words_list) эту часть закомментировал ведь ранее 1000 слов уже сохранились в файл

bot.polling()

