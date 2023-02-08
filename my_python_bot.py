import telebot

token = '5682555678:AAHBky5nVTQfrvoCZdNZJjZqUch0tE7N0eg'

bot = telebot.TeleBot(token)

from random import choice

import telebot

token = ''

bot = telebot.TeleBot(token)


RANDOM_TASKS = ['Написать Гвидо письмо', 'Выучить Python', 'Записаться на курс в Нетологию', 'Посмотреть 4 сезон Рик и Морти']

todos = dict()


HELP = '''
Список доступных команд:
* print  - напечать все задачи на заданную дату
* todo - добавить задачу
* random - добавить на сегодня случайную задачу
* help - Напечатать help
'''


def add_todo(date, task):
    date = date.lower()
    if todos.get(date) is not None:
        todos[date].append(task)
    else:
        todos[date] = [task]


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, HELP)


@bot.message_handler(commands=['random'])
def random(message):
    task = choice(RANDOM_TASKS)
    add_todo('сегодня', task)
    bot.send_message(message.chat.id, f'Задача {task} добавлена на сегодня')


@bot.message_handler(commands=['add'])
def add(message):
    _, date, tail = message.text.split(maxsplit=2)
    task = ' '.join([tail])
    add_todo(date, task)
    bot.send_message(message.chat.id, f'Задача {task} добавлена на дату {date}')


@bot.message_handler(commands=['show'])
def print_(message):
    date = message.text.split()[1].lower()
    if date in todos:
        tasks = ''
        for task in todos[date]:
            tasks += f'[ ] {task}\n'
    else:
        tasks = 'Такой даты нет'
    bot.send_message(message.chat.id, tasks)


bot.polling(none_stop=True)








#@bot.message_handler(content_types=["text"])
#def echo(message):
#    if message.text == "Игорь":
#        bot.send_message(message.chat.id, "Привет, Игорян!")
#    elif message.text.lower() == "ярослава":
#        bot.send_message(message.chat.id, "Привет, Ясенька!")
#    elif message.text.lower() == "привет":
#        bot.send_message(message.chat.id, "Привет, Человек!")
#    elif message.text.lower() == "как дела?":
#        bot.send_message(message.chat.id, "Да ничего, потихоньку. Думаю о своём создателе, Игоре.")
#    else:
        bot.send_message(message.chat.id, "Я пока не научился отвечать на это сообщение(((")
    #bot.send_message(message.chat.id, message.text)


bot.polling(none_stop=True)