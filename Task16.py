# Задача 16: Требуется вычислить, сколько раз встречается 
# некоторое число X в массиве A[1..N]. Пользователь в первой 
# строке вводит натуральное число N – количество элементов в 
# массиве. В последующих строках записаны N целых чисел Ai. 
# Последняя строка содержит число X.
#*Пример:*
# 5
# 1 2 3 4 5
# 3
# -> 1

import random

N = int(input("Введите длину массива: "))
list_test = []
for i in range(N):
    list_test.append(random.randint(-N, N + N // 2))

print(list_test)
X = int(input("Введите искомое число: "))
count = 0
for i in list_test:
    if i == X:
        count += 1

print(f"-> {count}")
