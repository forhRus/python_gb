# Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности.

import random

my_list = [random.randint(0, 10) for i in range(10)]
print(my_list)
unic_list = []

for item in my_list:
    if not item in unic_list:
        unic_list.append(item)
else:
    unic_list.sort()

print(unic_list)

#читерский вариант
my_set = set(my_list)
print(my_set)
