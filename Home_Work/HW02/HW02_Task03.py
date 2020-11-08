while True:
    user_month = int(input("Введите месяц в виде целого числа от 1 до 12: "))
    if user_month > 12:
        print("Вы ввели невалидное значение!")
    else:
        break
# Решение через list
# month_list = [[12, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]]
#
# if user_month in month_list[0]:
#     print("Зима")
# elif user_month in month_list[1]:
#     print("Весна")
# elif user_month in month_list[2]:
#     print("Лето")
# elif user_month in month_list[3]:
#     print("Осень")

# Решение через dict (не могу понять, почему не выводит значение)
month_dict = {"Зима": (12, 1, 2), "Весна": (3, 4, 5), "Лето": (6, 7, 8),
              "Осень": (9, 10, 11)}
for season, month in month_dict.items():
    if season == user_month:
        print(month)
