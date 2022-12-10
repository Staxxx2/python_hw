# Задайте список из N элементов, 
# заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.
# (для продвинутых - с файлом, вариант минимум 
# - ввести позиции в консоли)


# -2 -1 0 1 2
# Позиции: 0,1 -> 2

with open("file.txt", 'r') as f:
    position = f.read().split('\n')
position = list(map(int, position))
print("Введите число:")
n = int(input())
list = [i for i in range(-n,n+1)]
multi = 1
for pos in position:
    multi *= list[pos]
print(f"Позиция: {position}")
print(f"Список: {list}")
print(multi)
