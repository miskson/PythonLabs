import config
import telebot

bot = telebot.TeleBot(config.TOKEN)


class Restaurant:
    name = str
    address = dict
    photo = str

    def __init__(self, name=None, address=None, photo=None):
        self.name = name
        self.address = address
        self.photo = photo

    def __str__(self):
        return f"\n************************\n"\
               f"Name:{self.name}\n"\
               f"address:{self.address}\n"\
               f"photoPath:{self.photo}\n"

    def __repr__(self):
        return f"\n************************\n"\
               f"Name:{self.name}\n"\
               f"address:{self.address}\n" \
               f"photoPath:{self.photo}\n"



@bot.message_handler(commands=['start', 'help'])
def welcome_message(message):
    bot.reply_to(message, f"Hello {message.from_user.first_name}\n\n"
                          f"I am created to help you remember and locate nearby restaurants and cafes you like.\n\n"
                          f"/add - to add restaurant's name photo and location you would like to save.\n\n"
                          f"/list - to see the list of all saved palaces.\n\n"
                          f"/reset - to reset the list(this action will delete all previously saved locations).\n\n"
                          f"/nearby - to locate all of the restaurants near you in 500m radius.\n\n"
                          f"During any of these operation you can type 'cancel' to abort operation")

    restaurantsList[message.from_user.id] = []


@bot.message_handler(commands=['add'])
def add_request(message):
    try:
        restaurantsList[message.from_user.id].append(Restaurant())
        bot_msg = bot.send_message(message.chat.id, "Please, input restaurant's name.")
        bot.register_next_step_handler(bot_msg, add_name)

    except Exception as e:
        bot.send_message(message.chat.id, "Something went wrong. Input '/start' command and try again")


def add_name(message):
    try:
        if message.text.lower() == 'cancel':
            bot.reply_to(message, '/Add operation has been canceled.')
            del restaurantsList[message.from_user.id][-1]
            return

    except Exception as e:
        pass

    try:
        if message.text:
            restaurantsList[message.from_user.id][-1].name = message.text
            bot_msg = bot.send_message(message.chat.id, "Now, send me restaurant's location via 'send geo-position' option")
            bot.register_next_step_handler(bot_msg, add_address)
        else:
            raise Exception()

    except Exception as e:
        bot_msg = bot.send_message(message.chat.id, "Please, input name of restaurant."
                                                    "Or type 'cancel' to cancel operation.")
        bot.register_next_step_handler(bot_msg, add_name)


def add_address(message):
    try:
        if message.text.lower() == 'cancel':
            bot.reply_to(message, '/Add operation is canceled')
            del restaurantsList[message.from_user.id][-1]
            return

    except Exception as e:
        pass

    try:
        if message.location:
            print(message.location)
            restaurantsList[message.from_user.id][-1].address = message.location
            print(restaurantsList)
            bot.send_message(message.chat.id, "Now send me photo of the place.")
            bot.register_next_step_handler(message, add_photo)
        else:
            raise Exception()

    except Exception as e:
        bot.send_message(message.chat.id, "Something went wrong. Send me geo-position of restaurant again."
                                          "Or type 'cancel' to abort procedure.")
        bot.register_next_step_handler(message, add_address)


def add_photo(message):
    try:
        if message.text.lower() == 'cancel':
            bot.reply_to(message, '/Add operation is canceled')
            del restaurantsList[message.from_user.id][-1]
            return

    except Exception as e:
        pass

    try:
        if message.photo:
            restaurantsList[message.from_user.id][-1].photo = message.photo
            bot.send_message(message.chat.id, f'Restaurant "{restaurantsList[message.from_user.id][-1].name}" '
                                              f'has been successfully added to the list!')
            print(restaurantsList)

        else:
            raise Exception()

    except Exception as e:
        print("error")


@bot.message_handler(commands=['list'])
def show_all(message):
    try:
        if restaurantsList[message.from_user.id]:
            for i in restaurantsList[message.from_user.id]:
                bot.send_message(message.chat.id, i.name)
                bot.send_message(message.chat.id, i.address)
                bot.send_message(message.chat.id, i.photo)
        else:
            bot.send_message(message.chat.id, "Looks like there is nothing to display.")

    except Exception as e:
        bot.send_message(message.chat.id, "Something went wrong. Input '/start' command and try again")


if __name__ == '__main__':
    restaurantsList = {}

bot.polling(none_stop=True)
