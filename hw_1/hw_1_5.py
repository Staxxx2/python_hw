# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

# Пример:

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

print("Введите координаты x_a")
x_a = int(input())
print("Введите координаты y_a")
y_a = int(input())
print("Введите координаты x_b")
x_b = int(input())
print("Введите координаты y_b")
y_b = int(input())
print("Результат: ")
r = ((x_a - x_b)**2 + (y_a - y_b)**2)**0.5
print(r)