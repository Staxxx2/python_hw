#Напишите программу, которая принимает на вход цифру, обозначающую день недели, 
# и проверяет, является ли этот день выходным..

print("Введите день недели цифрой")
a = int(input())

if a >= 6 and a<= 7:
    print("Выходной день")
elif a > 0 and a <=5:
    print ("Будний день")
else:
    print("Ошибка!")
