# coding=utf-8


precision = 10


def by_midsearch(value):
    high = float(value)
    low = float(value) / 2
    while low * low > value:
        high = low
        low = low / 2

    prec = 1 / (10 ** precision)

    counter = 0
    while low != high:
        counter += 1
        mid = (low + high) / 2
        product = mid * mid

        if product == value:
            break
        if (high - mid) < prec:
            break
        if product < value:
            low = mid
        else:
            high = mid

    return low


def by_newton(value):
    # x^2 - value = 0
    # f(x) = x^2 - value
    # newton method to resolve sqrt

    # slope = 2 * x

    prec = 1 / (10 ** precision)
    x = value / 2
    while x * x > value:
        x = x / 2

    for counter in range(1000):
        if x * x == value:
            return x
        before = x
        x = x - (x * x - value) / (2 * x)
        if abs(before - x) < prec:
            break

    return x


if __name__ == '__main__':
    print(by_newton(2))
    print(by_midsearch(2))
