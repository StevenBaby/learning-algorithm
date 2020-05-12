# coding=utf-8


def generate_random_list(length=10):
    import random

    values = [var + 1 for var in range(length)]

    result = list()
    while values:
        value = random.choice(values)
        values.remove(value)
        result.append(value)

    return result
