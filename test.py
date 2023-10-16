my_str = str(input("Завдання №5. Введіть строку: "))
my_str = my_str + my_str[::-1] if len(my_str) < 5 else my_str
print(my_str)
