users_figure = int(input("Введите целое число от 1 до 10: "))

figure_two = int(str(users_figure) + str(users_figure))
figure_three = int(str(users_figure) + str(figure_two))

summary = users_figure + figure_two + figure_three

print(f"Расчет: {users_figure}+{figure_two}+{figure_three}={summary}")

