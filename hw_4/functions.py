# 4'. Задана натуральная степень k. 
# Сформировать случайным образом список 
# коэффициентов (значения от 0 до 100) 
# многочлена и записать в файл многочлен 
# степени k.

# Пример:

# k=2 => 2*x*2 + 4*x + 5 = 0 или x2 + 5 = 0 или 10*x*2 = 0
# k=3 => 2*x*3 + 4*x*2 + 4*x + 5 = 0 5'. 

import sympy
from random import randint as rnd

#функция генерации полинома
def create_polinom(k: int, simple: bool = True) -> str:
    polinom = ''
    for i in range(k, -1, -1):
        polinom += f'{rnd(0,2)}*x**{i}+'
        if i ==0:
            polinom += f'{rnd(0, 100)}*x**{i}'
    if simple:
        return str(sympy.simplify(polinom))
    else:
        return str(polinom)

#функция записи в файл
def create_pol_files(polinom: str, filename: str = 'new'):
    with open(f'hw_4/{filename}.txt', 'w') as f:
        f.write(polinom)

print(f'Введите степень к: ')
k = int(input())

print(f'Сгенерированный полином {create_polinom(k)}')
print(f'Сгенерированный полином {create_polinom(k, False)}')
create_pol_files(create_polinom(k))




