import telebot
import config
import requests
from bs4 import BeautifulSoup as BS

r = requests.get("https://weather.com/ru-RU/weather/today/l/RSXX0063:1:RS")
html = BS(r.content, 'html.parser')

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['weather'])
def weather(message):
    for el in html.select("#todayDetails"):
        t = el.select(".WeatherDetailsListItem--wxData--23DP5")[0].text

        w = el.select(".WeatherDetailsListItem--wxData--23DP5")[1].text
        w = w.replace('Wind Direction', '')

        wet = el.select(".WeatherDetailsListItem--wxData--23DP5")[2].text

        p = el.select(".WeatherDetailsListItem--wxData--23DP5")[4].text
        p = p.replace("Arrow Down", '')
        p = p.replace("Arrow Up", '')
    bot.send_message (message.chat.id, "Max./Min. - " + t)
    bot.send_message (message.chat.id, "Wind - " + w)
    bot.send_message (message.chat.id, "Wet - " + wet)
    bot.send_message (message.chat.id, "Pressure - " + p)

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
