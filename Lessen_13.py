# Написати клас та реалізувати його методи: (основа – ДЗ № 10)
#
# 1. Ініціалізація класу з одним параметром – ім'я файлу.

# 2. Написати метод екземпляра класу, який створює атрибут екземпляра класу
# у вигляді списку рядків (назви повертати без крапки)
#

# class SurnameParser:
#
#     def __init__(self, filename):
#         self.filename = filename
#
#     def get_surnames(self):
#         with open(self.filename, "r") as f:
#             surnames = []
#             for line in f:
#                 surname = line.split("\t")[1]
#                 surname = surname.strip().replace(".", "")
#                 surnames.append(surname)
#         self.surnames = surnames
#         return surnames
#
#
# surname_parser = SurnameParser("names.txt")
# surnames = surname_parser.get_surnames()
# print(surnames)

# 2. Написати метод екземпляра класу, який повертає список усіх прізвищ із файлу.
# Кожен рядок файлу містить номер, прізвище, країну, кілька (таблиця взята з вікіпедії).
# Розділювач - символ табуляції "t"

# class SurnameParser:
#
#     def __init__(self, filename):
#         self.filename = filename
#
#     def get_surnames(self):
#         with open(self.filename, "r") as f:
#             surnames = []
#             for line in f:
#                 surname = line.split("\t")[1]
#                 surname = surname.strip().replace(".", "")
#                 surnames.append(surname)
#         return surnames
#
#
# surname_parser = SurnameParser("names.txt")
# surnames = surname_parser.get_surnames()
# print(surnames)


#
# 3. Написати метод екземпляра класу, який повертає список
# словників виду {"date": date} у яких date - це дата з рядка (якщо є),
# Наприклад [{"date": "1st January 1919"}, {"date": "8th February 1828"}, ...]
#

# class DateParser:
#
#     def __init__(self, filename, event_type):
#         self.filename = filename
#         self.event_type = event_type
#
#     def get_dates(self):
#         dates = []
#         with open(self.filename, "r") as f:
#             for line in f:
#                 if line.startswith("#"):
#                     continue
#                 if self.event_type in line:
#                     date = line.split("-")[0]
#                     dates.append({"date": date})
#         return dates
#
#
# filename = "authors.txt"
# event_type = "birthday"
# date_parser = DateParser(filename, event_type)
# dates = date_parser.get_dates()
# print(dates)


# 4* (*здавати не обов'язково).
# Написати метод екземпляра класу, отримує у вигляді параметра ім'я файлу (authors.txt) та повертає список
# словників виду {"date_original": date_original, "date_modified": date_modified}
# у яких date_original - це дата з рядка (якщо є),
# а date_modified - ця ж дата, представлена у форматі "dd/mm/yyyy" (d-день, m-місяць, y-рік)
# Наприклад [{"date_original": "8th February 1828", "date_modified": 08/02/1828}, ...]
