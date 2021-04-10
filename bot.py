import telebot
import config
import requests
from bs4 import BeautifulSoup as BS

r = requests.get("https://sinoptik.ua/погода-москва")
html = BS(r.content, 'html.parser')

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['weather'])
def weather(message):
    for el in html.select("#blockDays"):
        t_min = el.select(".temperature .min")[0].text
        t_max = el.select(".temperature .max")[0].text
    bot.send_message (message.chat.id, "Min temperature - " + str(t_min) + "\nMax temperature - " + str(t_max))

@bot.message_handler(commands=['start'])
def hello(message):
    bot.send_message (message.chat.id, "Hello, stranger! type /help to know all my abilities")

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message (message.chat.id, "U can try this commands: \n /start \n /help \n /fuck \n /weather")

@bot.message_handler(commands=['fuck'])
def fuck(message):
    bot.send_message (message.chat.id, "Yea, fuck me please, mmmah")

@bot.message_handler(content_types=['text'])
def repeat(message):
    bot.send_message(message.chat.id, message.text)

bot.polling(none_stop=True)
