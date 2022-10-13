# Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

from random import randint
from unittest import result

def list(n):
    if n <= 10 and n>=1:
        return [randint(1, 10) for i in range(n)]
    else:
        print("Введено неверное значение")
    exit()

def unic_number(list):
    return [i for i in set(list)]

n = int(input('Введите число от 1 до 10: '))

result = list(n)
print(result)
print(unic_number(result))