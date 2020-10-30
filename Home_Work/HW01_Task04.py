figure = str(int(input("Введите целое положительное число: ")))

figures_list = []

i = 0
max_el = 0
while i <= len(figure)-1:
    position = figure[i]
    if int(position) > max_el:
        max_el = int(position)
    figures_list.append(position)
    i += 1
print(max_el)
print(figures_list)






