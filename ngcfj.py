# Напишите рекурсивную функцию, которая
# раскладывает натуральное число на простые сомножители.
#
g = list()
def funk(x):
    if x == 1:
        return
    t = x
    for i in range(2, x+1):
        if x % i == 0:
            g.append(i)
            break
    funk(t//i)
funk(int(input()))
print(print(g))