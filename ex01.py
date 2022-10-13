# Вычислить число π c заданной точностью d.

from unittest import result

num = input('Введите число d: ')
d = len(num) - num.find('.')
result = sum(1/16**x*(4/(8*x + 1) - 2/(8*x + 4) - 1/(8*x + 5) - 1/(8*x + 6)) for x in range(d))

print(str(result)[:len(num)])