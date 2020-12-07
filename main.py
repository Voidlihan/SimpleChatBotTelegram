import random

import telebot
import os
from telebot import types

bot = telebot.TeleBot('')


@bot.message_handler(commands=['start'])
def handle_start(message):
    user_mark = telebot.types.ReplyKeyboardMarkup(True, False)
    user_mark.row('/start', '/stop', '/help')
    user_mark.row('картинка', 'видео')
    user_mark.row('аудио', 'локация')
    bot.send_message(message.chat.id, 'Начнем! Это бот, который выполнит разные команды. Подробности в /help', reply_markup=user_mark)


@bot.message_handler(commands=['stop'])
def handle_start(message):
    hide_mark = telebot.types.ReplyKeyboardRemove()
    bot.send_message(message.from_user.id, '...', reply_markup=hide_mark)


@bot.message_handler(commands=['help'])
def start_message(message):
    user_mark = telebot.types.ReplyKeyboardMarkup(True, False)
    user_mark.row('/start', '/stop', '/help')
    user_mark.row('картинка', 'видео')
    user_mark.row('аудио', 'локация')
    bot.send_message(message.chat.id, 'Выполняю несколько различных команд. Ты можешь написать боту "Привет", "Пока", "Кто ты?", "Кто создатель?" а он даст тебе ответ. Умею отправлять аудио, видео, картинки и определить локацию.', reply_markup=user_mark)


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == 'Привет':
        bot.send_message(message.chat.id, 'Салам!')
    elif message.text == 'Пока':
        bot.send_message(message.chat.id, 'Прощай!')
    elif message.text == 'Кто ты?':
        bot.send_message(message.chat.id, 'Я бот, который будет выполнять несколько команд.')
    elif message.text == 'Кто создатель?':
        bot.send_message(message.chat.id, 'Алихан Есентай')
    elif message.text == 'картинка':
        directory = r'C:\Users\ealih\Desktop\Задачи, проекты, файлы\stars'
        all_files_in_dir = os.listdir(directory)
        random_file = random.choice(all_files_in_dir)
        img = open(directory + '/' + random_file, 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_photo')
        bot.send_photo(message.from_user.id, img)
        img.close()
    elif message.text == 'аудио':
        audio = open(r"C:\Users\ealih\Downloads\5431670a4d22385.mp3", 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_audio')
        bot.send_audio(message.from_user.id, audio)
        audio.close()
    elif message.text == 'локация':
        bot.send_chat_action(message.from_user.id, 'find_location')
        bot.send_location(message.from_user.id, 51.128137, 71.430390)
    elif message.text == 'видео':
        video = open(r"C:\Users\ealih\Desktop\Задачи, проекты, файлы\damenane.mp4", 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_video')
        bot.send_video(message.from_user.id, video)
        video.close()
    elif message.text == 'never gonna':
        img = open(r'C:\Users\ealih\Desktop\Задачи, проекты, файлы\nevergonna.jpg', 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_photo')
        bot.send_photo(message.from_user.id, img)
        bot.send_message(message.chat.id, 'give you up')
        img.close()
    elif message.text == 'kek':
        img = open(r'C:\Users\ealih\Desktop\Задачи, проекты, файлы\shrek.jpg', 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_photo')
        bot.send_photo(message.from_user.id, img)
        bot.send_message(message.chat.id, 'somebody once told me the world is gonna roll me')
        img.close()
    elif message.text == 'u got that':
        img = open(r'C:\Users\ealih\Desktop\Задачи, проекты, файлы\ricardo.jpg', 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_photo')
        bot.send_photo(message.from_user.id, img)
        img.close()
    elif message.text == 'nigga':
        img = open(r'C:\Users\ealih\Desktop\Задачи, проекты, файлы\nigga.gif', 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_document')
        bot.send_document(message.from_user.id, img)
        bot.send_message(message.chat.id, 'its okay nigga')
        img.close()
    else:
        bot.send_message(message.chat.id, 'Я тебя не понял.')


bot.polling(none_stop=True, interval=0)