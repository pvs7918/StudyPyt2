# 1. Напишите программу, которая принимает на вход два числа
#    и проверяет, является ли одно число квадратом другого.


a=int(input('Введите a'))
b=int(input('Введите b'))

if a*a == b or b*b == a:
    print('является')
else:
    print('не является')