import config
import telebot

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def welcome_message(message):
    bot.reply_to(message, f"Hello {message.from_user.first_name}\n\n"
                          f"I am created to help you remeber and locate nearby restaurants and cafes you like.\n\n"
                          f"/add - to add restaurant's name photo and location you would like to save.\n\n"
                          f"/list - to see the list of all saved palaces.\n\n"
                          f"/reset - to reset the list(this action will delete all previously saved locations).\n\n"
                          f"/nearby - to locate all of the restaurants near you in 500m radius.")
    print(message.from_user)

bot.polling(none_stop=True)
