words = ['антарктида', 'амплитуда', 'локомотив', 'индустриализация', 'рыбалка', 'гиппопотама', 'журналистика', 'конституция', 'клавиатура', 'металлургия', 'наказание', 'электричество', 'фразеологизм', 'территория']
from random import choice, shuffle
import random
word = choice(words).lower()
shuffle_word = list(word)
shuffle(shuffle_word)
a = 0
from MyTokennumber import TOREN
import telebot
bot = telebot.TeleBot(TOREN)
@bot.message_handler(content_types = ['text'])
def otvet_na_text(message):
    global a
    if a == 0:
        bot.send_message(message.chat.id,"Угадай слово: "+ ''.join(shuffle_word) +'\t')
        a = 1
        message.text.lower().split()

    else:

        if message.text == word:
            bot.send_message(message.chat.id,"Угадал")
            bot.send_message(message.chat.id,"#"*30)
            a = 0

        else:
            bot.send_message(message.chat.id,"Не Угадал")


bot.polling()
