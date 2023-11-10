# Homework 15 by Polskoi Yuri


def num(str_num):
    negative = str_num[0] == '-'
    new_num = str_num
    if negative:
        if len(str_num) == 1:
            return f'Ви ввели некоректне число: {str_num}'
        new_num = str_num[negative:]

    int_part = '0'
    dec_part = ''
    dec_num = False

    for i in new_num:

        if i in {'.', ','}:
            if not dec_num:
                dec_num = True
                continue
            else:
                return f'Ви ввели некоректне число: {str_num}'

        if not i.isdigit():
            return f'Ви ввели некоректне число: {str_num}'

        if dec_num:
            dec_part = dec_part.__add__(i)
        else:
            int_part = int_part.__add__(i)

    sign = "від'ємне" if negative else "додатне"
    if dec_num:
        if not dec_part:
            return f'Ви ввели некоректне число: {str_num}'
        if int(dec_part) != 0:
            return f'Ви ввели {sign} дробове число: {float(("-" if negative else "") + str(int(int_part)) + "." + dec_part)}'

    return f'Ви ввели {sign} ціле число: {int(int_part)}' if int(int_part) != 0 else 'Ви ввели нуль'


while True:
    input_str = input("Введіть число або або 'вихід', 'exit', 'quit', 'e', 'q'  для виходу: ")
    if input_str.lower() in ("вихід", "exit", "quit", "e", "q"):
        break
    if input_str == "":
        continue
    print(num(input_str))
