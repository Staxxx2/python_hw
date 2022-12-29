# Задача: предложить улучшения кода для уже решённых задач:

# С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension
# (выбрать 3 любые)


#hw 4.1
# 1'. Вычислить число Пи c заданной 
# точностью d

# *Пример:* 

# - при d = 0.001, π = 3.141
# - при d = 0.0001, π = 3.1415  

from math import pi

def get_pi(acc: float) -> float:
    acc = str(acc)
    acc = len(acc[acc.find('.')+1::])
    print("Введеная точность: ")
    print(acc)
    return acc

d = input("Введите точность (в формате 0.001): ")
acc_lambda = get_pi(d)  
pi_lambda = pi
func_lambda = lambda pi_lambda, acc_lambda: float(f'{pi_lambda:0.{acc_lambda}f}')

print(func_lambda(pi_lambda, acc_lambda))



