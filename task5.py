# Напишите функцию, которая «переворачивает» число,
# то есть возвращает число, в котором цифры стоят в обратном порядке.
# Вводится натуральное число
# Пользоваться input()[::-1] запрещено!
# Идея задачи реализовать алгоритм,
# который будет работать для любого введенного натурального числа.

def down_up(num):
    if num<10:
        return str(num)
    else:
        return str(num%10)+down_up(num//10)
print(down_up(int(input())))

def invariant(n):
    answer = ''
    for i in range(len(str(n))):
        num = str(n)[(-i-1)]
        answer = answer + num
    return answer
number=int(input())    
print(invariant(number))

