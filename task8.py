# Напишите рекурсивную функцию, которая
# раскладывает натуральное число на простые сомножители.
#
# Пример:
# Ввод:
# 378
# Вывод:
# 2*3*3*3*7

def resheto(N):    # Решето эратосфена
     primes = [i for i in range(N + 1)]
     primes[1] = 0

     for i in range(2, N//2+1):
        if primes[i] != 0:
            for j in range(i+i, N+1, i):
                primes[j] = 0



     return [i for i in primes if i != 0]
n=int(input())
simple=resheto(n)
print(simple)
for num in simple:
    if n%num==0:
        print(num)
        n=n//num