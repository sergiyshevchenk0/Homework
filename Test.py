import time


def sum_numbers(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i
    return sum


def measure_execution_time(code):
    start_time = time.time()
    exec(code)
    end_time = time.time()
    execution_time = end_time - start_time
    return execution_time


code = '''
result = sum_numbers(100000000)
print("Сумма чисел:", result)
'''

execution_time = measure_execution_time(code)
print(f"Время выполнения кода: {execution_time} секунд")
