# Всі пункти зробити як окремі функції та їх виклики.
#
# 1. Написати функцію, яка отримує як параметр ім'я файлу назви інтернет доменів (domains.txt)
# та повертає їх у вигляді списку рядків (назви повертати без крапки).

# filename = 'Homework/domains.txt'
# def get_domains(filename):
#     with open(filename, "r") as f:
#         domains = f.readlines()
#     domains = [domain.strip().replace(".", "") for domain in domains]
#     return domains
#
# domains = get_domains("domains.txt")
# print(domains)

# 2. Написати функцію, яка отримує як параметр ім'я файла (names.txt)
# і повертає список усіх прізвищ із нього.
# Кожен рядок файлу містить номер, прізвище, країну, кілька (таблиця взята з вікіпедії).
# Розділювач - символ табуляції "t"

# filename = 'Homework/names.txt'
# def get_all_surnames(filename):
#     with open(filename, "r") as f:
#         surnames = []
#         for line in f:
#             surname = line.split("\t")[1]
#             surnames.append(surname)
#     return surnames
#
#
# surnames = get_all_surnames("names.txt")
# print(surnames)

# 3. Написати функцію, яка отримує у вигляді параметра ім'я файлу (authors.txt) та повертає список
# словників виду {"date": date}
# у яких date - це дата з рядка (якщо є),
# Наприклад [{"date": "1st January 1919"}, {"date": "8th February 1828"}, ...]

# filename = 'Homework/authors.txt'
#
# def get_dates(filename, event_type):
#     with open(filename, "r") as f:
#         dates = []
#         for line in f:
#             if line.startswith("#"):
#                 continue
#             if event_type in line:
#                 date = line.split("-")[0]
#                 dates.append({"date": date})
#     return dates
#
#
# filename = "authors.txt"
# event_type = "birthday"
# dates = get_dates(filename, event_type)
#
# print(dates)

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#
# 4* (*здавати не обов'язково).
# Написати функцію, яка отримує у вигляді параметра ім'я файлу (authors.txt) та повертає список
# словників виду {"date_original": date_original, "date_modified": date_modified}
# у яких date_original - це дата з рядка (якщо є),
# а date_modified - ця ж дата, представлена у форматі "dd/mm/yyyy" (d-день, m-місяць, y-рік)
# Наприклад [{"date_original": "8th February 1828", "date_modified": 08/02/1828}, ...]
