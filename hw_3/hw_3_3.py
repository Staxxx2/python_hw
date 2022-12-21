# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу 
# между максимальным и минимальным значением 
# дробной части элементов.

# *Пример:*

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19


def separate(num: float) -> float:
    list = str(num).split('.')
    return float('0'+list[1])

def max_vs_min(num_list: list[float]) -> float:
    new_list = [separate(i) for i in num_list if int(i) != float(i)]
    print(new_list)
    return max(new_list) - min(new_list)

a = [1.31, 1.21, 3.3, 5, 10.01]

print(max_vs_min(a))