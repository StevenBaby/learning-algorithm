# coding=utf-8


def max(*values):
    if not values:
        return None
    m = values[0]
    for var in range(1, len(values)):
        if values[var] > m:
            m = values[var]
    return m


def min(*values):
    if not values:
        return None
    m = values[0]
    for var in range(1, len(values)):
        if values[var] < m:
            m = values[var]
    return m


def min_max(*values):
    if not values:
        return None, None

    length = len(values)
    min_value = float('inf')
    max_value = -min_value

    for i in range(0, length, 2):
        j = i + 1

        v1 = values[i]
        if j >= length:
            v2 = values[i]
        elif values[j] > v1:
            v2 = values[j]
        else:
            v2 = v1
            v1 = values[j]

        if v1 < min_value:
            min_value = v1
        if v2 > max_value:
            max_value = v2

    return min_value, max_value
