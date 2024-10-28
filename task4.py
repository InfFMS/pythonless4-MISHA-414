# Напишите функцию, которая находит
# наибольший общий делитель двух натуральных чисел
# На входе два числа, на выходе их НОД.

a, b=map(int, input().split())
def ma(a, b):
    maxim=1
    for num in range(1, max(a, b)+1):
        if a%num==0 and b%num==0:
           maxim=num
    return maxim
print(ma(a, b))