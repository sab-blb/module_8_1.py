print(f'{"Задание"} {"«Программистам всё можно»"}')

def add_everything_up(a, b):
    try:
        result = a + b
        if isinstance(result, float):
            return "{:.3f}".format(result)
        return result
    except TypeError:
        return str(a) + str(b)

# Примеры использования

print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
