# try, except, finaly, else

# try:
#     intput_num = int(input())
#     num = 13 / intput_num
#     print(num)
# except ValueError as err:
#     print("mistake", err)

# try:
#     intput_num = int(input())
#     num = 13 / intput_num
#     print(num)
# except ZeroDivisionError as err:
#     print(err)
# else:
#     print("Correct")
# finally:
#     print("the end")


# try:
#     a = open("text.txt", "r")
# except FileNotFoundError:
#     a = open("text.txt", "a+")
#
#     for i in range(1, 101):
#         a.write(f"{i} ")
#     a.seek(0)
#     print(a.read())
#     a.close()

from random import *

# a = randint(1, 16)
# print(a)

# random_number = random()
# print(round(random_number, 2))

# range_random = randrange(1, 15, 2)
# print(range_random)

# listok = ["apple", "banana", "pen", "octopus"]
# print(choice(listk))
# shuffle(listok)
# print(listok)
# print(choices(listok, [6, 3, 2, 1], k=15))


# files = open("text.txt", "r")
# list_names = files.read().split("\n")
# counter = 0
# while True:
#     name = choice(list_names)
#     counter += 1
#     list_names.remove(name)


