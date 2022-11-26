"""
 Пользователь вводит целое положительное число. Найдите самую большую цифру в
 числе. Для решения используйте цикл while и арифметические операции
"""
user_number = int(input("Введите целое положительное число :"))
max_value = 0
while user_number > 0:
    count = user_number % 10
    if max_value < count:
        max_value = count
    user_number = user_number // 10
print(f"Самая большая цифра в числе :{max_value}")
