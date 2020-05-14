# coding=utf-8


def bernouli(times=10000):
    import random

    inner = 0
    for _ in range(times):
        x = random.random()
        y = random.random()
        distance = x * x + y * y
        if distance <= 1:
            inner += 1

    pi = inner * 4 / times
    return pi


def chudnovsky(precision=100, type=str):
    """Calculating PI by Chudnovsky formula

    1 / pi = (1 / 53360 sqrt(640320)) sum(
        (-1)^k * (6k)! / ((k!)^3 * (3k)!  ) *
        (13591409 + 545140134 * k) / 64320^(3k)
    )

    sqrt(640320) = 8 * sqrt(10005)
    53360 * sqrt(640320) = 426880 * sqrt(10005)

    pi = (426880 * sqrt(10005)) / (
        (-1)^k * (6k)! / ((k!)^3 * (3k)!  ) *
        (13591409 + 545140134 * k) / 64320^(3k)
    )


    Keyword Arguments:
        precision {int} -- (default: {10})
        type {type} -- [result type] (default: {'string'})

    Returns:
        if type == str: return string
        if type == int: return int
    """

    from .sqrt import sqrt

    precise = precision + 2
    carry = 10**precise

    # Start Calculating
    sqrt_10005 = sqrt(10005, precise, type=int)
    product = 13591409 * carry
    amend = 1

    fact_6k = 1
    fact_k3 = 1
    fact_3k = 1

    upper = 13591409
    under = 1

    sign = 1
    k = 0
    while abs(amend) > 0:
        sign *= -1
        k += 1

        var = 6 * k
        fact_6k *= var * (var - 1) * (var - 2) * (var - 3) * (var - 4) * (var - 5)

        fact_k3 *= k ** 3

        var = 3 * k
        fact_3k *= var * (var - 1) * (var - 2)

        upper += 545140134
        under *= 262537412640768000  # 640320 ** 3

        amend = (fact_6k * upper * carry) // (fact_k3 * fact_3k * under)
        product += sign * amend

    result = 426880 * sqrt_10005 * carry // product // 100

    if type == int:
        return result

    result = str(result)
    result = result[:-precision] + "." + result[-precision:]
    return result
