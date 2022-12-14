# Напишите программу, которая найдёт 
# произведение пар чисел списка. 
# Парой считаем первый и последний элемент, 
# второй и предпоследний и т.д.

# *Пример:*

# - [2, 3, 4, 5, 6] =>[12,15,16]      ([2*6, 3*5, 4*4]);
# - [2, 3, 5, 6] => [12,15]   ( [2*6, 3*5]) 

# p.s. В скобках пример, как это работает!!!


def get_nums(nums: list[int]) -> list:
    pairs = []
    rang = int(round((len(nums)+1)/2))
    for i in range(rang):
        pairs.append(nums[i]*nums[len(nums)-1-i])
    return pairs


a = [2, 3, 4, 5, 6, 5]
print(f"Число: {a}")
print(f"Произведение: ")
print(get_nums(a))

