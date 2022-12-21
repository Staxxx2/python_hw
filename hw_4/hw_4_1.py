# 1'. Вычислить число Пи c заданной 
# точностью d

# *Пример:* 

# - при d = 0.001, π = 3.141
# - при d = 0.0001, π = 3.1415  

from math import pi

def get_pi(num: float, acc: float) -> float:
    acc = str(acc)
    acc = len(acc[acc.find('.')+1::])
    print("Введеная точность: ")
    print(acc)
    return float(f'{pi:0.{acc}f}')
    

d = input("Введите точность (в формате 0.001): ")
print(f"Pi: {get_pi(pi, d)}")
