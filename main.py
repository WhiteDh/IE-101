from telebot import types
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import table
import datetime

TOKEN = '5720241024:AAH15FGeeyQUHJRBRbds9yYGp1_7_KCF8z8'

bot = telebot.TeleBot(TOKEN)
count = 0
markdown = "*bold text*"


def day_of_week(date):
    if date.weekday() == 0:
        return "Понеділок"
    elif date.weekday() == 1:
        return "Вівторок"
    elif date.weekday() == 2:
        return "Середа"
    elif date.weekday() == 3:
        return "Четвер"
    elif date.weekday() == 4:
        return "П'ятниця"
    elif date.weekday() == 5:
        return "Субота"
    elif date.weekday() == 6:
        return "Неділя"


def show_day(date):
    if date.isocalendar()[1] % 2 == 0:
        week = "Нижній"
        time_table = table.nep_week
    else:
        week = "Верхній"
        time_table = table.par_week

    return f"<b>{week}\n{day_of_week(date)}, {date.day}.{date.month}.{date.year}:</b>\n\n{time_table[date.weekday()]}"


def show_today(message, today):
    markup = InlineKeyboardMarkup()
    next_day = types.InlineKeyboardButton("наступний день", callback_data=f'next_day{today}')
    prev_day = types.InlineKeyboardButton("попередній день", callback_data=f'prev_day{today}')
    markup.add(prev_day, next_day)
    bot.send_message(message.chat.id, show_day(today), parse_mode="HTML", reply_markup=markup,
                     disable_web_page_preview=True)


def show_this_week(message):
    today = datetime.datetime.today() - datetime.timedelta(datetime.datetime.weekday(datetime.datetime.today()))
    for i in range(0, 7):
        bot.send_message(message.chat.id, show_day(today + datetime.timedelta(i)), parse_mode="HTML",
                         disable_web_page_preview=True)


def show_next_week(message):
    today = datetime.datetime.today() - datetime.timedelta(
        datetime.datetime.weekday(datetime.datetime.today())) + datetime.timedelta(7)
    for i in range(0, 7):
        bot.send_message(message.chat.id, show_day(today + datetime.timedelta(i)), parse_mode="HTML",
                         disable_web_page_preview=True)


def next_day(message, day):
    today = datetime.datetime.today()
    today = datetime.date(int(day[0:4]), int(day[5:7]), int(day[8:10])) + datetime.timedelta(1)

    markup = InlineKeyboardMarkup()
    next_day = types.InlineKeyboardButton("наступний день", callback_data=f'next_day{today}')
    prev_day = types.InlineKeyboardButton("попередній день", callback_data=f'prev_day{today}')
    markup.add(prev_day, next_day)

    bot.edit_message_text(show_day(today), chat_id=message.chat.id, message_id=message.id, parse_mode="HTML",
                          reply_markup=markup, disable_web_page_preview=True)


def prev_day(message, day):
    today = datetime.datetime.today()
    file_log = open('log.txt', 'a')
    today = datetime.date(int(day[0:4]), int(day[5:7]), int(day[8:10])) - datetime.timedelta(1)

    markup = InlineKeyboardMarkup()
    next_day = types.InlineKeyboardButton("наступний день", callback_data=f'next_day{today}')
    prev_day = types.InlineKeyboardButton("попередній день", callback_data=f'prev_day{today}')
    markup.add(prev_day, next_day)

    bot.edit_message_text(show_day(today), chat_id=message.chat.id, message_id=message.id, parse_mode="HTML",
                          reply_markup=markup, disable_web_page_preview=True)


def show_buttons(message):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    today = types.KeyboardButton(text="сьогодні")
    this_week = types.KeyboardButton(text="цей тиждень")
    next_week = types.KeyboardButton(text="наступний тиждень")
    markup.add(today)
    markup.add(this_week, next_week)
    bot.send_message(message.chat.id, "туцяй кнопки", reply_markup=markup)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    show_buttons(message)



@bot.message_handler(content_types=['text'])
def message_reply(message):
    today = datetime.datetime.today()

    if message.text == "сьогодні" or message.text =="сегодня":

        show_today(message, today)

    elif message.text == "цей тиждень" or message.text == "эта неделя":
         show_this_week(message)



    elif message.text == "наступний тиждень" or message.text == "следующая неделя":
        show_next_week(message)



@bot.callback_query_handler(func=lambda call: True)
def iq_callback(call):
    if call.data[0:8] == "next_day":
        day = call.data[8:]
        next_day(call.message, day)


    if call.data[0:8] == "prev_day":
        day = call.data[8:]
        prev_day(call.message, day)



bot.polling(none_stop=True)


