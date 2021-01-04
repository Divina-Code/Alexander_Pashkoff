import telebot
import random
count = random.randint(0, 100)
bot = telebot.TeleBot('1488309812:AAEQfBGPxx6NkB5cSEud4WpEJz2GyPX7H_4')
@bot.message_handler(content_types = ['text'])
def otvet_na_text(message):
    global count
#    bot.send_message(message.chat.id, count)
    message.text.lower().split()
    if str(message.text) == "return":
        bot.send_message(message.chat.id, "OKAY")
        count = random.randint(0, 100)

    elif int(message.text) == count:
        bot.send_message(message.chat.id, "It is")
        count = random.randint(0, 100)
        bot.send_message(message.chat.id, "#" * 30)
        bot.send_message(message.chat.id, "YOU GUESS THE NUMBER")

    elif int(message.text) > count:

        bot.send_message(message.chat.id, "Take less")
    elif int(message.text) < count:

        bot.send_message(message.chat.id,"Take more")


bot.polling()
