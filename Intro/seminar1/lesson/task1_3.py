# 3. Напишите программу, которая будет на вход принимать
# число N и выводить числа от -N до N

N = int(input('Введите N: '))
#for i in range(-N, N+1):
#    print(i)

print(*list(range(-N,N+1)))