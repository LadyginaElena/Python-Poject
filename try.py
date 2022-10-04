# def smash(words):
#     return f"{words}"
#
#
# smash(['hello', 'world', 'this', 'is', 'great'])

#
# def abbrev_name(name):
#     list = name.split(" ")
#     new_list=list.split()
#     print(new_list)


name = "Саша Белый"
def abbrev_name(name):
    tuple_1 = name.split(" ")
    a = str(tuple_1[0])
    b = str(tuple_1[1])
    tuple_2 = tuple(a)
    tuple_3 = tuple(b)
    c = (tuple_2[0])
    d = (tuple_3[0])
    return f'{c.upper}.{d.upper}'

print(abbrev_name("Саша Белый"))

# def move(position, roll):
#     # your code here
#     return f'move({position}, {roll}) should equal'
#
#
# move(3, 6)
#
#
# # 4521369741 → you have to find the sum of this numbers until it’s a single-digit number.
# # Like this : 4 + 5 +2 +1 + 3 + 6 + 9 + 7+ 4 + 1 = 42 > 4 + 2 = 6 ( output )

# number = 352
# digit_1 = number % 10
# digit_2 = (number % 100) // 10
# digit_3 = number // 100
# print(digit_1)
# print(digit_2)
# print(digit_3)
