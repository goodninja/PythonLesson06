# Берём уже пройденную задачу: Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

# Используем List Comprehension

def multipliers_list_for_N(n):
    if n > 0:
        result = [x for x in range(1, n+1) if not n % x]
        print(f'Список множителей числа {n} следующий: \n {result}')
    else:
        print("Необходимо ввести натуральное число")

def input_N():
    num = int(input('Задайте натуральное число N: '))
    multipliers_list_for_N(num)

input_N()