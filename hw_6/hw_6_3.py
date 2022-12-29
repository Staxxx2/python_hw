#  Задайте число. Составьте список чисел Фибоначчи, 

n = 10

def fib(n):
    if n in [1,2]:
        return 1
    elif n == 0:
        return 0
    else:
        return fib(n-1) + fib(n-2)

list_comprehension = [fib(i) for i in range(1, n+1)]


print(list_comprehension)

list_map = list_comprehension

#не знал куда применить третью функцию и решил умножить на 2 все числа из задачи применив map
list_map = list(map(lambda i:i*2, list_map))
print(list_map)