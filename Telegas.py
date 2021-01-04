import telebot
import random
count = random.randint(0, 100)
bot = telebot.TeleBot('1488309812:AAEQfBGPxx6NkB5cSEud4WpEJz2GyPX7H_4')
@bot.message_handler(content_types = ['text'])
def otvet_na_text(message):
    global count
    bot.send_message(message.chat.id, count)
    message.text.lower().split()
    if int(message.text) == count:
        bot.send_message(message.chat.id, "It is")
        count = random.randint(0, 100)
    elif message.text.lower() == "return":
        count = random.randint(0, 100)
        bot.send_message(message.chat.id, "Take less")
    elif int(message.text) > count:
        bot.send_message(message.chat.id, "Take less")
    elif int(message.text) < count:
        bot.send_message(message.chat.id,"Take more")
    else:
        bot.send_message(message.chat.id,"It is not")



bot.polling()
