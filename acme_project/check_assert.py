def series_sum(incoming):
    # Конкатенирует все элементы списка, приводя их к строкам.
    result = ''
    for i in incoming:
        result += str(i)
    return result

call = series_sum([1, 1.1, 2])

print(series_sum([1, 1.1, 2]))
