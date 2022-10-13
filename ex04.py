# Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.

def my_func(stroke, find):
    if stroke.count(find) > 1:
        k = stroke.index(find)
        print(stroke.index(find, k+len(find)))
    else:
        print(-1)

stroke = list(map(str, input('Введите символы через пробел: \n').split()))
print(stroke)
find = input("Какую строку необходимо найти?:")
my_func(stroke, find)