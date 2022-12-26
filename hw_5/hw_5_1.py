# На выбор:
# 1. Создайте программу для игры с конфетами
# человек против человека.

# *' Условие задачи:
# На столе лежит 117 конфета. Играют два игрока делая
# ход друг после друга.
# Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.


# a) Добавьте игру против бота


# Игрок1 вс игрок2


import random
candys = 117


def input_candy():
    global candys
    while True:
        print('введите целое число от 1 до 28 включительно')
        move = int(input('Введите конфеты: '))
        if move > 0 and move < 29 and move <= candys:
            candys -= move
            break
        else:
            print('Необходимо ввести число от 1 до 28 включительно')


print(f'На столе лежит {candys} конфет')
players = ['Игрок1', 'Игрок2']
print('Бросаю монетку')
move = random.choice(players)
print(f'Первым ходит - {move}')
while True:
    if move == 'Игрок1':
        input_candy()
        print(f'Осталось {candys}')
        move = 'Игрок2'
        if candys < 29:
            print(f'Победил {move}')
            break
    if move == 'Игрок2':
        input_candy()
        print(f'Осталось {candys}')
        move = 'Игрок1'
        if candys < 29:
            print(f'Победил {move}')
            break
