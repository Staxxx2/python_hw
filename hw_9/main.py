# # Добавить игру, реализованную ранее, с конфетами к боту.
# # *' Условие игры: На столе лежит 117 конфета.
# #  Играют два игрока делая ход друг после друга. 
# # Первый ход определяется жеребьёвкой. 
# # За один ход можно забрать не более чем 28 конфет. 
# # Все конфеты оппонента достаются сделавшему последний ход.
# import telebot



import random

import telebot
# Создаем экземпляр бота
bot = telebot.TeleBot('5964532083:AAEaQjadfJDc00xArKUOUglGu9jrODYzQfQ')
# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'На столе лежит 117 конфет')
    bot.send_message(m.chat.id, 'Введите целое число от 1 до 28 включительно')
    bot.send_message(m.chat.id, 'Введите количество конфет: ')
    print("message_handler()")


# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def handle_text(message):
    global ok, candys
    candys = 117
    move = int(message.text)
    print(move)
    print("candys")
    print(candys)
    while candys >= 0:
        bot.send_message(message.chat.id, 'Введите целое число от 1 до 28 включительно')
        bot.send_message(message.chat.id, 'Введите количество конфет: ')
        print(candys)
        ok = input_candy(move)  # c или 1(все ок) или 0
        print(ok)
        
        while True:
            print("while")    
            if ok == 1:
                candys = candys - move
                bot.send_message(message.chat.id,"Осталось " + str(candys) + " конфет")
                break
            else:
                print("c == 1")
                bot.send_message(message.chat.id, 'Необходимо ввести число от 1 до 28 включительно')
                bot.send_message(message.chat.id, 'Введите количество конфет: ')
                ok = input_candy(move)  #если ошибка в вводе повторно вызываем функцию input_candy
                break
        print("OK")
        break

def input_candy(message):
    print("input_candy()")
    if int(message) > 0 and int(message) < 29 and int(message) <= candys:        
        a = 1
        return a
    else:
        a = 0
        return a


bot.polling(none_stop=True, interval=0)
