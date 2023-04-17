# Задача 18: Требуется найти в массиве A[1..N] самый близкий 
# по величине элемент к заданному числу X. Пользователь в первой 
# строке вводит натуральное число N – количество элементов в 
# массиве. В последующих строках записаны N целых чисел Ai. 
# Последняя строка содержит число X.
# *Пример:*
# 5
# 1 2 3 4 5
# 6
# -> 5

import random

N = int(input("Введите длину массива: "))
list_test = []
for i in range(N):
    list_test.append(random.randint(-N, N + N // 2))

print(list_test)

X = int(input("Введите число: "))
val = list_test[0]
max_val = abs(X - list_test[0])

set_test = set(list_test)
for i in set_test:
    t = abs(X - i)
    if t < max_val:
        max_val = t
        val = i

print(f"-> {val}")
