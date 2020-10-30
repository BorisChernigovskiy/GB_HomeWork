first_day_result = float(input("Сколько километров Вы пробежали в первый день? "))
planning_result = float(input("Введите целевой показатель в километрах, к которому стремитесь: "))

kilometers = []
days = []

kilometers.append(first_day_result)
days.append(1)

other_days_counter = 1

while True:
    if other_days_counter == 1:
        next_day_result = float(first_day_result + (first_day_result * 0.1))
        kilometers.append('{:.2f}'.format(next_day_result))
        other_days_counter += 1
        days.append(other_days_counter)
        if next_day_result >= planning_result:
            break
    elif other_days_counter > 1:
        next_day_result = float(next_day_result + (next_day_result * 0.1))
        kilometers.append('{:.2f}'.format(next_day_result))
        other_days_counter += 1
        days.append(other_days_counter)
        if next_day_result >= planning_result:
            break

print(f"Вы достигли цели на {other_days_counter} день!")
print(days, kilometers)
