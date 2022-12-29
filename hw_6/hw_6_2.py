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