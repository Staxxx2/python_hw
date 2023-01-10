import requests # Модуль для обработки URL
from bs4 import BeautifulSoup # Модуль для работы с HTML
import telebot
from telebot import types


# Создаем экземпляр бота
bot = telebot.TeleBot('5964532083:AAEaQjadfJDc00xArKUOUglGu9jrODYzQfQ')

# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(m, res=False):
    markup = types.ReplyKeyboardMarkup()
    itembtna = types.KeyboardButton('USD') #предлагаем пользователю выбор валюты, оставил одну USD
    markup.row(itembtna)
    bot.send_message(m.chat.id, "Choose one letter:", reply_markup=markup)
    print(markup)


@bot.message_handler(content_types=["text"])
def handle_text(message):
    
    url = 'https://www.banki.ru/products/currency/cb/' #url страницы для парсинга
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    string = str(soup.find_all(class_='standard-table standard-table--row-highlight'))# получаем страницу
    string_parce_usd = string[string.find('США</strong>\n</a>'):string.find('red">'):].replace(',', '.') #парсим раз
    string_complete_usd = string_parce_usd[string_parce_usd.find('</td>\n<td>'):string_parce_usd.find('<td class'):].replace(',', '.')#парсим два
    usd_price_index = string_complete_usd.find('<td>') #парсим три, ищем индекс <td> 
    usd_price = string_complete_usd[usd_price_index+4] + string_complete_usd[usd_price_index+5] + string_complete_usd[usd_price_index+6] + string_complete_usd[usd_price_index+7] + string_complete_usd[usd_price_index+8] #5 символов справа от td наша стоимость
    bot.send_message(message.chat.id,"Цена USD = " + str(usd_price))

bot.polling(none_stop=True, interval=0)