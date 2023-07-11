import telebot
import webbrowser
from telebot import types

bot = telebot.TeleBot('5414349911:AAHmv7s5SQaDsfz3tkFYGN4KRu6FVlvGvIQ')

@bot.message_handler(commands=['git', 'github'])
def site(message):
    webbrowser.open('https://github.com/rudepe4eneg')

@bot.message_handler(commands=['start', 'main', 'hello'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('GitHub')
    markup.row(btn1)
    file = open('./photo.jpeg', 'rb')
    audio = open('ЗА ДЕНЬГИ ДА.mp3', 'rb')
    bot.send_photo(message.chat.id, file)
    bot.send_audio(message.chat.id, audio)
    bot.send_message(message.chat.id, f'Hello, {message.from_user.first_name}', reply_markup=markup)
    bot.register_next_step_handler(message, on_click)

def on_click(message):
    if message.text == 'GitHub':
        bot.send_message(message.chat.id, 'GitHub page is open')


@bot.message_handler(commands=['help'])
def main(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Перейти на сайт', url='https://github.com/rudepe4eneg'))
    bot.send_message(message.chat.id, '<b><u>Help Information:</u></b>'
                                      ' This bot was created by @gogoshawty.'
                                      ' For more information, write @gogoshawty.'
                                      ' GitHub page:', parse_mode='html', reply_markup=markup)

@bot.message_handler()
def info(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, f'Hello, {message.from_user.first_name}')
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'ID {message.from_user.id}')

@bot.message_handler(content_types=['photo', 'video'])
def get_photo(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Delete photo', callback_data='delete')
    markup.row(btn1)
    bot.reply_to(message, 'Looks great!', reply_markup=markup)

@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'delete':
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)
        bot.delete_message(callback.message.chat.id, callback.message.message_id)

bot.infinity_polling()