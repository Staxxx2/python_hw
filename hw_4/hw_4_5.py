# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

# В file1.txt :
# 2*x**2 + 4*x + 5

# В file2.txt:
# 4*x**2 + 1*x + 4

# Результирующий файл:
# 6*x**2 + 5*x + 9

from functions import create_polinom
from functions import create_pol_files
from sympy import simplify

degree = int(input('задайте степень: '))

#создаем полиномы
pol1 = create_polinom(degree)
pol2 = create_polinom(degree)

#имена файлов
filename1 = 'first'
filename2 = 'second'
sum_filename = 'sum'

create_pol_files(pol1, filename1)
create_pol_files(pol1, filename2)

with open(f'hw_4/{filename1}.txt','r') as f1:
    f_pol = f1.read()
    print(f'Первый полином: {f_pol}')

with open(f'hw_4/{filename1}.txt','r') as f2:
    s_pol = f2.read()
    print(f'Первый полином: {s_pol}')

sum_of_pols = simplify(f_pol + '+' + s_pol)
sum_of_pols = str(sum_of_pols)

print(f'Сумма: {sum_of_pols}')

with open(f'hw_4/{sum_filename}.txt', 'w') as s:
    s.write(sum_of_pols)



