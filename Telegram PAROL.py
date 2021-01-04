from MyTokennumber import TOREN
import telebot
import random
bot = telebot.TeleBot(TOREN)
@bot.message_handler(content_types = ['text'])

def otvet_na_text(message):
    if str(message.text.lower()) == "start":
        letter = list("abcdefghigklmnopqrstuvwxz!@#$%^&*_+-*/`1234567890")
        massiv = []
        for q in range(8):
            a = letter[random.randint(0, 48)]
            massiv.append(a)
    bot.send_message(message.chat.id, " ".join(massiv))

bot.polling()
