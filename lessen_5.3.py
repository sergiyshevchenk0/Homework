# 3. Користувач вводить окремо рядок `s` та один символ `ch`. Необхідно здійснити пошук у рядку `s` всіх символів `ch`.
# Для вирішення можна використовувати тільки функцію `find` (rfind), оператори `if` та `for` (while).

s = input("Введіть строку: ")
ch = input("Введіть літеру для пошуку: ")
found_letters = []
index = 0
while index < len(s):
    if s[index] == ch:
        found_letters = found_letters + [(ch, index)]
    index += 1
print("Знайдені літери та їх индекси:")
for letter, index in found_letters:
    print(f"Літера '{letter}' знайдена по індексу {index}")