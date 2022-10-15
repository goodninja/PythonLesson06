# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# *Пример:*
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

def mult_numbers(numbers):
    if numbers.replace(" ", "").isdigit():
        numbers_list = numbers.split(" ")
        processing_list = list(map(int,numbers_list))
        result = []
        i = 0
        while i < len(processing_list) / 2:
            result.append(processing_list[i]*processing_list[len(processing_list)-1-i])
            i += 1
        print(f'Произведение пар чисел списка \n{result}')
    else:
        print("Необходимо задать список чисел")

def input_numbers():
    list = input('Задайте список чисел \nВведите числа через пробел -> ')
    mult_numbers(list)

input_numbers()