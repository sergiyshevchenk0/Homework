# 1. Написати функцію яка приймає один параметр – список рядків my_list. Функція повертає новий список у якому міститься
# елементи з my_list за таким правилом:
# Якщо рядок стоїть на непарному місці my_list, то його замінити на перевернутий рядок. "qwe" на "ewq".
# Якщо на парному – залишити без зміни.

# def revers_elements(my_list):
#
#   new_list = []
#   for index, i in enumerate(my_list):
#     if index % 2 == 0:
#       new_list.append(i[::-1])
#     else:
#       new_list.append(i)
#   return new_list
#
# my_list = ["qwe", "asd", "zxc", "qwe"]
# new_list = revers_elements(my_list)
# print(new_list)

# 2. Написати функцію яка приймає один параметр – список рядків my_list.
# Функція повертає новий список у якому міститься елементи my_list у яких перший символ - буква "a".

# def first_letter_a(my_list):
#   new_list = []
#   for i in my_list:
#     if i[0] == "a":
#       new_list.append(i)
#   return new_list
#
# my_list = ["qwe", "asd", "zxc", "qwe"]
# new_list = first_letter_a(my_list)
# print(new_list)

# 3. Написати функцію яка приймає один параметр – список рядків my_list.
# Функція повертає новий список у якому міститься елементи з my_list, у яких є символ - буква "a" на будь-якому місці.

# def letter_a(my_list):
#
#   new_list = []
#   for i in my_list:
#     if "a" in i:
#       new_list.append(i)
#   return new_list
#
# my_list = ["qwe", "asd", "zxc", "qawe"]
# new_list = letter_a(my_list)
# print(new_list)

# 4. Написати функцію яка приймає один параметр - список рядків my_list у якому може бути як рядки (type str) і цілі
# числа (type int). Функція повертає новий список у якому містяться лише рядки з my_list.
# Приклад використання функції:

# def get_strings_list(my_list):
#
#   new_list = []
#   for i in my_list:
#     if type(i) == str:
#       new_list.append(i)
#   return new_list
#
# my_list = ["John", 15, "Sergei", 37, "Poll", 38]
# new_list = get_strings_list(my_list)
# print(new_list)
#
# 5. Написати функцію яка приймає один параметр – рядок my_str.
# Функція повертає новий список у якому містяться ті символи з my_str, які зустрічаються у рядку лише один раз.

# def only(my_str):
#   new_list = []
#   for i in my_str:
#     if i not in new_list:
#       new_list.append(i)
#   return new_list
#
# my_str = "asdasdasdasdasdasd"
# new_list = only(my_str)
# print(new_list)

# 6. Написати функцію яка приймає один параметр - два рядки.
# Функція повертає список у який помістити ті символи, які є в обох рядках хоча б один раз.

# def get_2_symbols(my_str1, my_str2):
#   new_list = []
#   for i in my_str1:
#     if i in my_str2:
#       new_list.append(i)
#   return new_list
#
# my_str1 = "qweasdzxcRTY"
# my_str2 = "asdzxcqwe"
# new_list = get_2_symbols(my_str1, my_str2)
# print(new_list)

# 7. Написати функцію яка приймає два параметри - два рядки.
# Функція повертає список до якого входять ті символи, які є в обох рядках, але в кожному лише по одному разу.
#
# def get_symbols(my_str1, my_str2):
#
#   new_list = []
#   for i in my_str1:
#     if i in my_str2 and i not in new_list:
#       new_list.append(i)
#   return new_list
#
# my_str1 = "qweasdzxcRTY"
# my_str2 = "qweasdzxc"
# new_list = get_symbols(my_str1, my_str2)
# print(new_list)

# 8. Дано списки names та domains (створити самостійно). Написати функцію для генерування e-mail у форматі:
#     "ім'я . число від 100 до 999 @ стрінга з літер довжиною від 5 до 7 символів . домен"
# Прізвище та домен брати випадковим чином із заданих списків переданих у функцію у вигляді параметрів.
# Рядок і число генерувати випадковим чином.
#
# Приклад використання функції:
#
# names = ["king", "miller", "kean"]
# domains = ["net", "com", "ua"]
# e_mail = create_email(domains, names)
# print(e_mail)
#
# Відповідь: miller.249@sgdyyur.com

import random
from string import ascii_uppercase

# def create_email(names, domains):
#     name = random.choice(names)
#     number = random.randint(100, 999)
#     string = "".join(random.choice(ascii_uppercase) for _ in range(5, 7))
#     return f"{name}.{number}@{string}.{random.choice(domains)}"
#
# names = ["king", "miller", "kean"]
# domains = ["net", "com", "ua"]
# e_mail = create_email(domains, names)
# print(e_mail)

