user_seconds = int(input("Введите время в секундах: "))

hours = float(user_seconds / 3600)

minutes = (hours - int(hours)) * 60

seconds = (minutes - int(minutes)) * 60
seconds = int(seconds)

if int(hours) == 24:
    hours = 00
hours = int(hours)
minutes = int(minutes)

if int(hours) > 24:
    print("Время нельзя расчитать, так как выходит за рамки 24 часового формата")
else:
    print(f"Полученное время: {hours}:{minutes}:{seconds}!")
