#Задание 2.1
health = int(input("Введите очки здоровья"))
if health <= 0:
    print("False")
else:
    print("True")
#Задание 2.2
a = int(input("Введите целое число"))
if a%2==0:
    print("Четное")
else:
    print("Нечетное")
#Задание 2.3
year = int(input("Введите год"))
if year%4==0 and year%100!=0 or year%400==0:
    print("Високосный")
else:
    print("Не високосный")
#Задание 2.4
text=input("Введите текст")
a=int(input("Количество повторов текста"))
print(text*a)
# через цикл while
i=int(input("Количество повторов текста"))
while i>0:
    print(i, text)
    i=i-1
# через цикл for
i1=int(input("Количество повторов текста"))
for i in range(i1):
    print(i, text)
