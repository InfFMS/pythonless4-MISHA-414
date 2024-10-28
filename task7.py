# Напишите функцию is_valid_triangle(side1, side2, side3),
# которая принимает в качестве аргументов три натуральных числа,
# и возвращает значение True, если существует невырожденный треугольник
# со сторонами side1, side2, side3, или False в противном случае.
def is_valid_triangle(side1, side2, side3):
    ma=max(side1, side2, side3)
    mi=min(side1, side2, side3)
    summ=side1+side2+side3
    duo=summ-ma-mi
    if ma>=mi+duo:
        print(False)
    else:
        print(True)

side1, side2, side3=map(int, input().split())
is_valid_triangle(side1, side2, side3)