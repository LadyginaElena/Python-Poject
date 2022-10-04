# Задание 3.1
# Дан список my_list = ['a', 'b', [1, 2, 3], 'd']. Распечатайте значения 1, 2, 3

my_list = ['a', 'b', [1, 2, 3], 'd']
list3=(my_list[2])
print(*list3, sep="\n")

print(my_list[2][0])
print(my_list[2][1])
print(my_list[2][2])

# Задание 3.2
# Дан список list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
#   - получите сумму всех чисел,
#   - распечатайте все строки, где есть буква 'a'

list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
a, b, c, d, e, f, j, i = list_1
print(c+e+j+i)

# lambda
print(sum(filter(lambda x: isinstance(x, int), list_1)))

# list comprehension
print([x for x in list_1 if isinstance(x, str) and 'a' in x])

# через цикл
list_sum=[]
for x in list_1:
    if type(x) == int:
        list_sum.append(x)
print(sum(list_sum))

new_list=[]
for x in list_1:
    if type(x) == str and "a" in x:
        new_list.append(x)
print(*new_list)


# Задание 3.3
# Превратите лист ['cat', 'dog', 'horse, 'cow'] в кортеж
l = ['cat', 'dog', 'horse', 'cow']
k = tuple(l)
print(k)

# Задание 3.4
# Напишите программу, которая определяет, какая семья больше.
#      1) Программа имеет два input() - например, family_1, family_2.
#      2) Членов семьи нужно перечислить через запятую.
#     Ожидаемый результат - программа выводит семью с бОльшим составом. Если состав одинаковый, print("Equal')

family_1 = input('Введите членов семьи 1 через запятую')
family_2 = input('Введите членов семьи 2 через запятую')
list_family_1 = family_1.split(",")
list_family_2 = family_2.split(",")
if len(list_family_1) == len(list_family_2):
    print("Equal")
elif len(list_family_1) > len(list_family_2):
    print(list_family_1)
elif len(list_family_1) < len(list_family_2):
    print(list_family_2)

# Задание 3.5
# Создайте словарь film c ключами title, director, year, budget, main_actor, slogan. В значения можете передать информацию
#    о вашем любимом фильме.
#    - распечатайте только ключи
#    - распечатайте только значения
#    - распечатайте пары ключ - значение
film = {
    "title" : "The Chronicles of Riddick",
    "director" : "David Twohy",
    "year" : "2004",
    "budget" : "$105 000 000",
    "main_actor" : "Vin Diesel",
    "slogan" : "Все силы во вселенной не смогут изменить судьбу"
}
print(film.keys())
print(film.values())
print(film.items())


# Задание 3.6
# Найдите сумму всех значений в словаре my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}

my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
a = sum(my_dictionary.values())
print(a)

# Задание 3.7
# Удалите повторяющиеся значения из списка [1, 2, 3, 4, 5, 3, 2, 1]
list2 = [1, 2, 3, 4, 5, 3, 2, 1]
set_1 = set(list2)
list2 = list(set_1)
print(list2)

# Задание 3.8
# Даны два множества: set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}, set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
# - найдите значения, которые встречаются в обоих множествах
# - найдите значения, которые не встречаются в обоих множествах
# - проверьте являются ли эти множества подмножествами друг друга

set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}
set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
print(set2.intersection(set1))
print(set2.symmetric_difference(set1))
print(set2.issuperset(set1))
print(set1.issubset(set2))
print(set2.issubset(set1))
