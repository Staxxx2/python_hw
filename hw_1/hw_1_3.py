# Напишите программу, которая принимает на вход 
# координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 
# и выдаёт номер четверти плоскости, 
# в которой находится эта точка 
# (или на какой оси она находится).

# Пример:

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3
print("Введите координаты Х")
x = int(input())
print("Введите координаты У")
y = int(input())
if x > 0 and y > 0:
    print("I")
elif x < 0 and y < 0:
    print("II")
elif x < 0 and y < 0:
    print("III")
elif x > 0 and y < 0:
    print("IV")
elif x == 0 and y == 0:
    print("Center")
elif x == 0:
    print("0x")
elif y == 0:
    print("0y")