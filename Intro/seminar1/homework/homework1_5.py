# Домашняя работа
# 5. Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.
# https://ru.onlinemschool.com/math/library/analytic_geometry/point_point_length/
# *Пример:*
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21
# ________________________________________
# in
# - 3
# - 6
# - 2
# - 1
# out
# 5.099
import math

x1 = float(input('X1: '))
y1 = float(input('Y1: '))
x2 = float(input('X2: '))
y2 = float(input('Y2: '))

dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
print(f'Расстояние между точками -> {dist:.3f}')
