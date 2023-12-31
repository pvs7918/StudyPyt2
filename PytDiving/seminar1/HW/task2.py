# 2.Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
# Дано a, b, c - стороны предполагаемого треугольника. Требуется сравнить длину каждого
# отрезка-стороны с суммой двух других. Если хотя бы в одном случае отрезок окажется больше
# суммы двух других, то треугольника с такими сторонами не существует. Отдельно сообщить
# является ли треугольник разносторонним, равнобедренным или равносторонним.

print('Введите стороны треугольника.')
a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))

if a > b + c:
    print('Это не треугольник. Сторона a больше суммы b и c.')
elif b > a + c:
    print('Это не треугольник. Сторона b больше суммы a и c.')
elif c > a + b:
    print('Это не треугольник. Сторона c больше суммы a и b.')
else:
    # это треугольник. Делаем доп.проверки его сторон
    equal_all_sides = False
    equal_two_sides = False

    if a == b and b == c:
        equal_all_sides = True
    elif a == b or b == c or a == c:
        equal_two_sides = True

    if equal_all_sides == True:
        print('Это равносторонний треугольник.')
    elif equal_two_sides == True:
        print('Это равнобедренный треугольник.')
    else:
        print('Это разносторонний треугольник.')
