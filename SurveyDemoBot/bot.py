# -*- coding: utf-8 -*-
import config
import telebot
from telebot import types


# создаем клавиатуру с оценками по шкале Лайкерта
markup = types.ReplyKeyboardMarkup()
markup.row('1 - Полностью не согласен','2 - Не согласен')
markup.row('3 - Затрудняюсь ответить')
markup.row('4 - Согласен','5 - Полностью согласен')


# создаем бота
bot = telebot.TeleBot(config.token)


# создаем опросник из утверждений в файле Affirmations.txt
questionnaire = []
f = open(config.path + 'Affirmations.txt', 'r')
for r in f:
    questionnaire.append(r)


@bot.message_handler(content_types=["text"])
def answer_the_question(message):
    f = open(config.path + 'Answers.txt', 'r')
    file_length = len(f.readlines())
    f.close()

    if message.text == '/start start' or message.text == '/start':
        test_question = questionnaire[0]
        f = open(config.path + 'Answers.txt', 'w')
        f.close()
    elif file_length == 0:
        f = open(config.path + 'Answers.txt', 'a')
        f.write(str(file_length) + ' - ' + message.text)
        test_question = questionnaire[file_length + 1]
    elif file_length == len(questionnaire):
        test_question = "Опрос завершен. Спасибо за участие!"
    else:
        f = open(config.path + 'Answers.txt', 'a')
        f.write('\n')
        f.write(str(file_length) + ' - ' + message.text)
        if file_length + 1 == len(questionnaire):
            test_question = "Опрос завершен. Спасибо за участие!"
        else:
            test_question = questionnaire[file_length + 1]
        f.close()
    bot.send_message(message.chat.id, test_question, reply_markup=markup)


if __name__ == '__main__':
    bot.polling(none_stop=True)
