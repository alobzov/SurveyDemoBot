# -*- coding: utf-8 -*-
import config
import os
import telebot
from telebot import types


# создаем клавиатуру с оценками по шкале Лайкерта
markup = types.ReplyKeyboardMarkup()
markup.row('1 - Полностью не согласен')
markup.row('2 - Не согласен')
markup.row('3 - Затрудняюсь ответить')
markup.row('4 - Согласен')
markup.row('5 - Полностью согласен')


# создаем бота
bot = telebot.TeleBot(config.token)


# создаем опросник из утверждений в файле Affirmations.txt
questionnaire = []
f = open(config.path + 'Affirmations.txt', 'r')
for r in f:
    questionnaire.append(r)


@bot.message_handler(content_types=["text"])
def answer_the_question(message):

    # формируем путь к файлу с ответами пользователя
    file_name = config.path + str(message.chat.id) + '_Answers.txt'

    # создаем файл с ответами в случае его отсутствия
    if os.path.exists(file_name):
        f = open(file_name, 'r')
    else:
        f = open(file_name, 'w+')
    file_length = len(f.readlines())
    f.close()

    # формируем сообщение для пользователя
    if message.text == '/start start' or message.text == '/start':
        test_question = questionnaire[0]
        f = open(file_name, 'w')
        f.close()
    elif message.text[0] not in ['1','2','3','4','5']:
        test_question = "Выбирете один из доступных ответов"
    elif file_length == 0:
        f = open(file_name, 'a')
        f.write(str(file_length) + ' - ' + message.text[0])
        test_question = questionnaire[file_length + 1]
    elif file_length == len(questionnaire):
        test_question = "Опрос завершен. Спасибо за участие!"
    else:
        f = open(file_name, 'a')
        f.write('\n')
        f.write(str(file_length) + ' - ' + message.text[0])
        if file_length + 1 == len(questionnaire):
            test_question = "Опрос завершен. Спасибо за участие!"
        else:
            test_question = questionnaire[file_length + 1]
        f.close()

    # отправляем сообщение пользователю
    bot.send_message(message.chat.id, test_question, reply_markup=markup)


if __name__ == '__main__':
    bot.polling(none_stop=True)
