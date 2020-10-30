earnings = float(input("Введите значение выручки фирмы: "))
costs = float(input("Введите значение издержек фирмы: "))

if earnings > costs:
    print("Фирма работает в прибыль!")
    print("Рентабельность выручки:{0}".format(float(earnings/costs)))
    empl = int(input("Укажите количество сотрудников фирмы: "))
    earnings_per_empl = float((earnings - costs) / empl)
    print(f"Прибыль фирмы в расчете на одного сотрудника:{earnings_per_empl}")
else:
    print("Фирма работает в убыток!")