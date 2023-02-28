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
difference_smaller_numbers = 0
difference_large_numbers = 0
if count_desired_number >= 1:
    print(count_desired_number)
else:
    for item in list:
        if item < desired_number:
            if difference_smaller_numbers == 0:
                difference_smaller_numbers = desired_number - item
                nearest_small_num = item
            else:
                if difference_smaller_numbers > desired_number - item:
                    difference_smaller_numbers = desired_number - item
                    nearest_small_num = item
        else:
            if difference_large_numbers == 0:
                difference_large_numbers = item - desired_number
                nearest_large_num = item
            else:
                if difference_large_numbers > item - desired_number:
                    difference_large_numbers = item - desired_number
                    nearest_large_num = item
if difference_large_numbers > difference_smaller_numbers:
    print(nearest_small_num)
else:
    print(nearest_large_num)
