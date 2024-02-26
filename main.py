# 1

# def calculate_number_summary(start, end):
#     even_sum = 0
#     odd_sum = 0
#     multiple_of_9_sum = 0
#     even_count = 0
#     odd_count = 0
#     multiple_of_9_count = 0
#
#     for num in range(start, end+1):
#         if num % 2 == 0:
#             even_sum += num
#             even_count += 1
#         else:
#             odd_sum += num
#             odd_count += 1
#
#         if num % 9 == 0:
#             multiple_of_9_sum += num
#             multiple_of_9_count += 1
#
#     even_avg =  even_sum / even_count if even_count > 0 else 0
#     odd_avg = odd_sum / odd_count if odd_count > 0 else 0
#     multiple_of_9_avg = multiple_of_9_sum / multiple_of_9_count if multiple_of_9_count > 0 else 0
#
#     return {
#         "even_sum": even_sum,
#         "odd_sum": odd_sum,
#         "multiple_of_9_sum": multiple_of_9_sum,
#         "even_avg": even_avg,
#         "odd_avg": odd_avg,
#         "multiple_of_9_avg": multiple_of_9_avg
#     }
#
# start = int(input("Введите начало диапазона: "))
# end = int(input("Введите конец диапозона: "))
#
# result = calculate_number_summary(start, end)
# print(result)


# 2


# x = input("Введите символ: ")
#
# for num in range(1, 5 +1):
#     print(x)


# # 3

# while True:
#     input_numbers = int(input("Введите числа: "))
#     if input_numbers == 7:
#         break
#     elif input_numbers > 0:
#         print("Number is positive")
#     elif input_numbers < 0:
#         print("Number is negative")
#     else:
#         print("Number is equal to zero")



# numbers = []
# sum_numbers = 0
# max_number = float('-inf')
# min_number = float('inf')
#
# while True:
#     num = int(input("Введите число: "))
#
#     if num == 7:
#         print("Good bye")
#         break
#
#     numbers.append(num)
#     sum_numbers += num
#     max_number = max(max_number, num)
#     min_number = min(min_number, num)
#
# print(f"Сумма введенных чисел: {sum_numbers}")
# print(f"Максимальное число: {max_number}")
# print(f"Минимальное число: {min_number}")