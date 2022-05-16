import telebot
from telebot import types
from config import TOKEN

bot = telebot.TeleBot(TOKEN)

# Create buttons
buttons = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
btn, btn1 = types.KeyboardButton("first btn"), types.KeyboardButton("sec btn")
buttons.add(btn, btn1)


# Start handler
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(
        message, "hello", reply_markup=buttons
    )


if __name__ == "__main__":
    bot.poling(none_stop=True)
