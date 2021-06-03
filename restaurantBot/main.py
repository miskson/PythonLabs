import config
import telebot

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def welcome_message(message):
    bot.reply_to(message, f"Hello {message.from_user.first_name}\n\n"
                          f"I am created to help you locating nearby restaurants and dines\n\n"
                          f"Also I save list of places you decided to add\n\n")
    print(message.from_user)

bot.polling(none_stop=True)
