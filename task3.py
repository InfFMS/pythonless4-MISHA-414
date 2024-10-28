# Напишите процедуру, которая выводит на экран
# запись переданного ей числа в римской системе счисления.
# Числа находятся в диапазоне [1, 3999]
# I - 1, V - 5, X - 10, L - 50, C  - 100, D - 500, M - 1000
# Пример:
# 2013
# MMXIII
num=int(input())

def Rome(n):
    if n==0:
        return ''
    elif n>=1000:
        n-=1000
        return 'M'+Rome(n)
    elif n>=500:
        n-=500
        return 'D'+Rome(n)
    elif n>=100:

        n-=100
        return 'C'+Rome(n)
    elif n>=50:

        n-=50
        return 'L'+Rome(n)
    elif n>=10:

        n-=10
        return 'X'+Rome(n)
    elif n>=5:

        n-=5
        return 'V'+Rome(n)
    else:

        n -= 1
        return 'I'+Rome(n)

print(Rome(num))