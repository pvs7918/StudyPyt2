numb = int(input('Введите число: '))
ost = abs(numb)
numlen = 1

while ost > 9:
    ost //= 10
    numlen += 1

res = 0
if numlen == 1:
    res = numb ** 2
elif numlen == 2:
    a = numb // 10
    b = numb % 10
    res = a * b
elif numlen == 3:
    a = numb // 100
    b = numb // 10 % 10
    c = numb % 10
    res = c * 100 + b * 10 + a

print(numb, numlen, res)
