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
    i = 2
    while i <= N:
        if primes[i] != 0:
            j = i + i
            while j <= N:
                primes[j] = 0
                j = j + i
        i += 1

    return [i for i in primes if i != 0]
n=int(input())
simple=resheto(n)
def Simp(n):

    for num in simple:
        if n == num:
            return num
        if n%num==0:
            n=n//num
            return f'{num}*{Simp(n)}'

print(Simp(n))