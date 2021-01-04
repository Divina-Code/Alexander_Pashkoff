from MyTokennumber import TOREN
import telebot
import random
count = random.randint(0, 100)
a = 0
bot = telebot.TeleBot(TOREN)
@bot.message_handler(content_types = ['text'])
def otvet_na_text(message):
    global count
    global a
#    bot.send_message(message.chat.id, count)
    message.text.lower().split()
    if str(message.text) == "return":
        bot.send_message(message.chat.id, "OKAY")
        count = random.randint(0, 100)
        a = 1

    elif int(message.text) == count:
        bot.send_message(message.chat.id, "It is")
        count = random.randint(0, 100)
        bot.send_message(message.chat.id, "#" * 30)
        bot.send_message(message.chat.id, "YOU GUESS THE NUMBER")
        bot.send_message(message.chat.id, a, "Attempts spent")
        a = 1
    elif int(message.text) > count:
        bot.send_message(message.chat.id, "Take less")
        a = a + 1

    elif int(message.text) < count:
        bot.send_message(message.chat.id,"Take more")
        a = a + 1


bot.polling()
