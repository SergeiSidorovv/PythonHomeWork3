# Первая задача:
# Задаем длину списка наполненного рандомными числами от 1 до 100.
# Вводим искомое число X
# Программа должна вывести в консоль сколько раз встречается в заданном списке искомое число X,
# которое мы вводим с клавиатуры, либо выводим на экран, максимально близкое ему по значению

import random

count_numbers = int(input("Введите количество чисел: "))
desired_number = int(input("Введите искомое число: "))

list = sorted([random.randint(0, 100) for _ in range(count_numbers)])
print(list)

count_desired_number = list.count(desired_number)
min_val = 0
max_val = 0
if count_desired_number >= 1:
    print(count_desired_number)
else:
    for item in list:
        if item < desired_number:
            if min_val == 0:
                min_val = desired_number - item
                min_res_val = item
            else:
                if min_val > desired_number - item:
                    min_val = desired_number - item
                    min_res_val = item
        else:
            if max_val == 0:
                max_val = item - desired_number
                max_res_val = item
            else:
                if max_val > item - desired_number:
                    max_val = item - desired_number
                    max_res_val = item
if max_val > min_val:
    print(min_res_val)
else:
    print(max_res_val)
