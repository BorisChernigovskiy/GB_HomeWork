figures = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

result = [
    value for i, value in enumerate(figures)
    if i > 0 and figures[i - 1] < value
]

print(result)