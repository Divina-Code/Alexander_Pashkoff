import telebot

bot = telebot.TeleBot('1488309812:AAEQfBGPxx6NkB5cSEud4WpEJz2GyPX7H_4')
@bot.message_handler(content_types=['text'])
def otvet_na_text(message):
    print(message)
    bot.send_message(message.chat.id, "Hello")



bot.polling()
