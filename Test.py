number = int(input("Введите 4-значное число: "))
print(number // 1000)  # Первая цифра
print((number % 1000) // 100)  # Вторая цифра
print((number % 100) // 10)  # Третья цифра
print(number % 10)  # Четвертая цифра
