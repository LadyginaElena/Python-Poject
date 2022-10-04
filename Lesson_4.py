# 4.1. Напишите функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения(с помощью кортежа):
# периметр квадрата, площадь квадрата и диагональ квадрата.
def square(a):
    return 4*a, a*a, a*(2**0.5),

print(square(6))

# 4.2. Напишите фукнцию, которая принимает произвольное количество именнованных аргументов и выводит их построчно
# в формате аргумент: значение. Например:
# name: John
# last_name: Smith
# age: 35
# position: web developer


def anketa(**keywords):
    for key, value in keywords.items():
        print(f"{key}: {value}")


anketa(name="John", last_name="Smith", age="35" , position= "web developer")


# 4.3.Используя лямбда - выражение, из списка
# my_list = [20, -3, 15, 2, -1, -21]
# создайте новый список, содержащий только положительные числа

my_list = [20, -3, 15, 2, -1, -21]
new_list = list(filter(lambda x: x > 0, my_list))
print(new_list)

# 4.4.Используя лямбда выражение, получите результат перемножения значений в предыдущем списке.
from functools import reduce
print(reduce(lambda x, y: x * y, new_list))

# 4.5.Создайте файл my_calc.py и пропишите в нем минимум 4 функции, выполняющие
# базовые арифметические вычисления. Примените эти функции в качестве методов в другом файле.
from my_calc import *
print(plus(10, 2))
print(minus(20, 5))
print(multip(5, 10))
print(divis(40, 4))
print(divis(1, 0))
