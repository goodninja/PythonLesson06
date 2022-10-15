# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# *Пример:*
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import re

def float_checking(str):
    try:
        float(str)
    except ValueError:
        return False
    return True

def list_checking(array):
    i = 0
    check = True
    while check and i < len(array):
        check = float_checking(array[i])
        i += 1
    return check

def min_max_difference(numbers):
    numbers_list = numbers.split(" ")
    if list_checking(numbers_list):
        processing_list = list(map(lambda x: re.sub(r'\d+\.', "0.", x),numbers_list))
        processing_list = list(map(float,processing_list))
        processing_list = list(filter(lambda x: x < 1, processing_list))
        print(processing_list)
        result = max(processing_list) - min(processing_list)
        print(f'Разница между максимальной и минимальной дробными частями элементов = {result}')
    else:
        print("Нужен список чисел!!!")

def input_numbers():
    list = input('Задайте список из вещественных чисел \nВводите числа через пробел (1.1 2.2 3.3 и т.д.) -> ')
    min_max_difference(list)

input_numbers()