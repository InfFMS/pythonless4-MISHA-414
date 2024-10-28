# Напишите функцию, которая сокращает дробь вида M/N.
# Где M и N - наутральные числа.
# В качестве аргументов она принимает числитель и знаменатель,
# выводит числитель и знаменатель после сокращения
#
# Пример:
# Ввод:
# 25 15
# Вывод:
# 5 3

a, b=map(int, input().split())
def razional(a, b):
    maxim=1
    for num in range(1, max(a, b)+1):
        if a%num==0 and b%num==0:
           maxim=num
    return a//maxim, b//maxim
print(razional(a, b))