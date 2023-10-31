# 1. Наведено список рядків my_list. Створити новий список до якого помістити елементи з my_list за таким правилом:
# Якщо рядок стоїть на непарному місці my_list, то його замінити на перевернутий рядок. "qwe" на "ewq".
# Якщо на парному – залишити без зміни. Завдання зробити за допомогою enumerate або range.

# my_list = ["qwe", "asd", "zxc", "qwe"]
# new_list = []
# for index, i in enumerate(my_list):
#     if index % 2 == 0:
#         new_list.append(i[::-1])
#     else:
#         new_list.append(i)
# print(new_list)

# 2. Наведено список рядків my_list. Створити новий список до якого помістити елементи my_list
# у яких перший символ - буква "a".

#
# my_list = ["qwe", "asd", "zxc", "qwe"]
# new_list = []
# for i in my_list:
#     if i[0] == "a":
#         new_list.append(i)
# print(new_list)

# 3. Наведено список рядків my_list. Створити новий список до якого помістити
# елементи з my_list, у яких є символ - буква "a" на будь-якому місці.

# my_list = ["qwe", "asd", "zxc", "qawe"]
# new_list = []
# for i in my_list:
#     if "a" in i:
#         new_list.append(i)
# print(new_list)

# 4) Даний список словників людей у форматі [{"name": "John", "age": 15}, ..., {"name": "Jack", "age": 45}]

                            # Відповідь 4a
# а) Створити список і помістити туди ім'я наймолодшої людини. Якщо вік збігається – помістити всі імена наймолодших.
# my_list = [
#     {"name": "John", "age": 15},
#     {"name": "Jack", "age": 45},
#     {"name": "Poll", "age": 38},
#     {"name": "Sergei", "age": 36},
#     ]
# new_list = []
# min_age = min(my_list, key=lambda x: x["age"])["age"]
# new_list = [i["name"] for i in my_list if i["age"] == min_age]
# print(new_list)

                            # Відповідь 4b
# б) Створити список та помістити туди найдовше ім'я. Якщо довжина імені збігається - помістити такі імена.
# my_list = [
#     {"name": "John", "age": 15},
#     {"name": "Jack", "age": 45},
#     {"name": "Poll", "age": 38},
#     {"name": "Sergei", "age": 36},
#     ]
# new_list = []
# max_name = max(my_list, key=lambda x: x["name"])["name"]
# new_list = [i["name"] for i in my_list if i["name"] == max_name]
# print(new_list)

                            # Відповідь 4в
# в) Порахувати середню вік усіх людей із початкового списку.
# my_list = [
#     {"name": "John", "age": 15},
#     {"name": "Jack", "age": 45},
#     {"name": "Poll", "age": 38},
#     {"name": "Sergei", "age": 36},
#     ]
# new_list = []
# for i in my_list:
#     new_list.append(i["age"])
# print(sum(new_list) / len(new_list))


# 5) Дано два словники my_dict_1 і my_dict_2.

                            # Відповідь 5a
# а) Створити список із ключів, які є в обох словниках.

# my_dict_1 = {"a": 1, "b": 2}
# my_dict_2 = {"c": 3, "a": 4}
# new_dict = []
# for i in my_dict_1.keys():
#     for j in my_dict_2.keys():
#         if i == j:
#             new_dict.append(i)
# print(new_dict)
                            # Відповідь 5б
# б) Створити список із ключів, які є у першому, але немає у другому словнику.

# my_dict_1 = {"a": 1, "b": 2}
# my_dict_2 = {"c": 3, "a": 4}
# new_dict = []
# for i in my_dict_1.keys():
#     if i not in my_dict_2.keys():
#         new_dict.append(i)
# print(new_dict)

                            # Відповідь 5в
# в) Створити новий словник з пар {ключ:значення} для ключів, які є в першому, але немає в другому словнику.

# my_dict_1 = {"a": 1, "b": 2}
# my_dict_2 = {"c": 3, "a": 4}
# new_dict = {}
# for i in my_dict_1.keys():
#     if i not in my_dict_2.keys():
#         new_dict[i] = my_dict_1[i]
# for i in my_dict_2.keys():
#     if i not in my_dict_1.keys():
#         new_dict[i] = my_dict_2[i]
# print(new_dict)

#                             # Відповідь 5г
# г) Об'єднати ці два словники у новий словник за правилом:
# якщо ключ є тільки в одному з двох словників - помістити пару ключ: значення,
# {1:1, 2:2}, {11:11, 2:22} ---> {1:1, 11:11, 2:[2, 22]}

# my_dict1 = {1: 1, 2: 2}
# my_dict2 = {11: 11, 2: 22}
# new_dict = {}
# for i in my_dict1.keys():
#     if i in my_dict2.keys():
#         new_dict[i] = [my_dict1[i], my_dict2[i]]
#     else:
#         new_dict[i] = my_dict1[i]
# for i in my_dict2.keys():
#     if i not in my_dict1.keys():
#         new_dict[i] = my_dict2[i]
# print(new_dict)