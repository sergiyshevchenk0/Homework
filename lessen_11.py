# Всі пункти є частиною одного завдання, тому можна використовувати функції кілька разів та не дублювати код.
# Якщо хочете, можете використовувати дефолтні значення та анотацію типів.
#
# 1. Написати функцію, яка отримує один параметр - ім'я директорії та повертає словник виду
# {'filenames': [список файлів у папці], 'dirnames': [список усіх підпапок у папці]}.
# Підпапки враховувати лише першого рівня вкладення. Папка в папці в папці - таке не брати))

import os


def get_directory_info(HomeWorkLessen_11_Directory):
    filenames = []
    dirnames = []
    for dirs, files in os.listdir():
        for filename in files:
            filenames.append(filename)
        for dirname in dirs:
            dirnames.append(dirname)
            break
    result = {'filenames': filenames, 'dirnames': dirnames}
    print(result)
    return result


# 2. Написати функцію, яка отримує два параметри – словник, описаний у пункті 1
# і значення булю (True/False) - можна зробити за замовчуванням.
# Функція повертає той самий словник, але з відсортованими іменами файлів та папок у відповідних списках.
# Булеве значення True означає, що порядок сортування алфавітний, False – зворотний порядок.
#
def sort_directory_info(directory_info, ascending=True):
    sorted_info = directory_info.copy()
    sorted_info['filenames'].sort(reverse=not ascending)
    sorted_info['dirnames'].sort(reverse=not ascending)
    return sorted_info


# 3. Написати функцію, яка отримує два параметри - словник, описаний у пункті 1 та рядок, який може бути
# або ім'ям файлу, або ім'ям папки. (У імені файлу має бути точка).
# Залежно від того, що функція отримала (ім'я файлу або ім'я папки) – записати його у відповідний список
# та повернути оновлений словник.
#

def update_directory_info(directory_info, name):
    if '.' in name:  # это файл
        directory_info['filenames'].append(name)
    else:  # это папка
        directory_info['dirnames'].append(name)
    return directory_info


# 4* (*здавати не обов'язково).
# Написати функцію, яка отримує два параметри - словник, описаний у пункті 1 та ім'я директорії.
# Функція перевіряє відповідність отриманого словника та реальної файлової системи в отриманій папці та,
# якщо треба, створює потрібні папки та порожні файли, відповідно до структури словника.


def synchronize_directory(directory_info, HomeWorkLessen_11_Directory):
    for filename in directory_info['filenames']:
        file_path = os.path.join(HomeWorkLessen_11_Directory, filename)
        if not os.path.isfile(file_path):
            open(file_path, 'a').close()
    for dirname in directory_info['dirnames']:
        dir_path = os.path.join(HomeWorkLessen_11_Directory, dirname)
        if not os.path.isdir(dir_path):
            os.mkdir(dir_path)
