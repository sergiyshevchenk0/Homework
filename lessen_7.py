# 1. Дано ціле число (int). Визначити скільки нулів у цьому числі.

            # Варіант 1
# namber = input("Введіть ціле число з нулями: ")
# count = 0
# for i in str(namber):
#   if i == "0":
#     count += 1
# print(count)

            # Варіант 2
# print(len([i for i in str(input("Введіть ціле число з нулями: ")) if i == "0"]))

            # Варіант 3
# number = 102003000
# string_number = str(number)
# count = string_number.count("0")
# print(count)

# 2. Дано ціле число (int). Визначити скільки нулів наприкінці цього числа. Наприклад для числа 1002000 - три нулі

# namber = int(input("Введіть ціле число з нулями: "))
# count = 0
# for i in str(namber)[::-1]:
#   if i == "0":
#     count += 1
#   else:
#     break
# print(count)

# 3. Дано списки my_list_1 та my_list_2.
# Створити список my_result, який спочатку помістити
# елементи на парних місцях my_list_1, а потім всі елементи на парних місцях my_list_2.

# my_list_1 = [1, 2, 3, 4, 5]
# my_list_2 = [6, 7, 8, 9, 10]
# my_result = []
# my_result.extend([i for i in my_list_1 if i % 2 == 0])
# my_result.extend([i for i in my_list_2 if i % 2 == 0])
# print(my_result)

# 4. Наведено список my_list. СТВОРИТИ НОВИЙ список new_list у якого перший елемент з my_list
# стоїть на останньому місці. Якщо my_list [1,2,3,4], то new_list[2,3,4,1]

# my_list = [7, 8, 9, 10]
# new_list = my_list[1:] + [my_list[0]]
# print(new_list)

# 5. Даний список my_list. У цьому списку перший елемент переставити на останнє місце.
# [1,2,3,4] -> [2,3,4,1]. Перестворювати список не можна! (використовуйте метод pop)

# my_list = [1, 2, 3, 4]
# element_1 = my_list.pop(0)
# my_list.append(element_1)
# print(my_list)

# 6. Дано рядок у якому є числа (розділяються пробілами).
# Наприклад "43 більше ніж 34, але менше ніж 56". Знайти суму ВСІХ ЧИСЕЛ (А НЕ ЦИФР) у цьому рядку.
# Для цього прикладу відповідь - 133. (використовуйте split та перевірку isdigit)

# value_str =" 56 > 43 > 34"
# def sum_all_nambers(value_str):
#   numbers = value_str.split()
#   sum = 0
#   for number in numbers:
#     if number.isdigit():
#       sum += int(number)
#   return sum
# print(sum_all_nambers(value_str))

# 7. Наведено список чисел. Визначте, скільки в цьому списку елементів,
# які більше суми двох своїх сусідів (ліворуч і праворуч), і НАДРУКАЙТЕ КІЛЬКІСТЬ таких елементів.
# Останні елементи списку ніколи не враховуються, оскільки у них недостатньо сусідів.
# Для списку [2,4,1,5,3,9,0,7] відповіддю буде 3, тому що 4> 2+1, 5> 1+3, 9>3+0.

# def sum_element(nambers):
#   count = 0
#   index = 1
#   while index < len(nambers) - 1:
#     if numbers[index] > numbers[index - 1] + numbers[index + 1]:
#       count += 1
#     index += 1
#   return count
# numbers = [2, 4, 1, 5, 3, 9, 0, 7]
# print(sum_element(numbers))

# 8. Даний список my_list, в якому можуть бути як рядки (type str), так і цілі числа (type int).
# Наприклад [1, 2, 3, "11", "22", 33]
# Створити новий список у який помістити лише рядки з my_list.

# my_list = [1, 2, 3, "11", "22", 33]
# new_list = []
# for i in my_list:
#     if type(i) == str:
#         new_list.append(i)
# print(new_list)

# 9. Дано рядок my_str. Створити список в який помістити символи з my_str,
# які зустрічаються в рядку ТІЛЬКИ ОДИН разів.
#
# my_str = ["1", "2", "3", "4", "5", "1", "2"]
# new_list = []
# for i in my_str:
#     if my_str.count(i) == 1:
#         new_list.append(i)
# print(new_list)

# 10. Дано два рядки. Створити список, у якому помістити ті символи,
# які є в обох рядках хоча б один раз.

# list_1 = ["1", "2", "3", "4", "5" ]
# list_2 = ["1", "6", "1", "7", "1" ]
# new_list = []
# for i in list_1:
#     if i in list_2:
#         new_list.append(i)
# print(new_list)

# 11. Дано два рядки. Створити список, у якому помістити ті символи, які є в обох рядках,
#
# str_1 = "aaaasdf1"
# str_2 = "asdfff2"
# new_list = []
# for i in str_1:
#    if i in str_2 and i not in new_list:
#       new_list.append(i)
# print(new_list)