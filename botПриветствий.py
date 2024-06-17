import telebot
#бот разработанный catfy для приветственных сообщений при первом заходе в группу, и при повторном входе если человек ранее выходил из группы.


token = "токен не укажу"

bot = telebot.TeleBot(token)

# Словарь для хранения информации о пользователях, покинувших группу
left_members = {}


def greet_user(message):
    for member in message.new_chat_members:
        if member.id not in left_members:
            bot.send_message(message.chat.id, f'Привет, {member.first_name}, добро пожаловать в группу!')

def greet_returning_members(message):
    for member in message.new_chat_members:
        if member.id in left_members:
            bot.send_message(message.chat.id, f"Привет снова, {member.first_name}! Рады видеть тебя снова в группе!")
            # Удаляем пользователя из словаря
            del left_members[member.id]

@bot.message_handler(content_types=["new_chat_members"])
def handle_new_members(message):
    greet_user(message)
    greet_returning_members(message)

@bot.message_handler(content_types=["left_chat_member"])
def handle_left_member(message):
    left_member = message.left_chat_member
    left_members[left_member.id] = True

if __name__ == '__main__':
    bot.infinity_polling()








