# Реализуйте алгоритм перемешивания списка.

from random import shuffle
from random import randint

mas = list(map(int, input().split()))
print(f'Список: {mas}')

print(f'новый список: {shuffle(mas)}')

for i in range(len(mas)-1):
    n = randint(0, len(mas)-1)
    mas[i], mas[n] = mas[n], mas[i]
print(mas)
