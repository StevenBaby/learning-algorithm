# coding=utf-8


def divide(result, upper, under, sign):
    change = False
    bit = 0

    while True:
        if upper == 0:
            break
        if upper < under:
            upper *= 10
            bit += 1
            continue

        if bit >= len(result):
            break

        adder = (result[bit] + (upper // under) * sign)
        upper = upper % under

        carry = adder // 10
        value = adder % 10
        result[bit] = value
        change = True

        if carry == 0:
            continue

        b = bit - 1
        while carry != 0 and b >= 0:
            adder = (result[b] + carry)
            carry = adder // 10
            value = adder % 10
            result[b] = value
            b -= 1

    return change


def merge(result):
    result.insert(1, '.')
    pi = ''.join([str(var) for var in result])
    return pi


def by_arctan(depth=300):

    result = [0 for var in range(depth + 1)]
    sign = -1
    var = -1

    while True:
        var += 2
        sign *= -1
        change = False
        for i in (2, 5, 8):
            under = (i ** var) * var
            upper = 4
            bit = 0

            change = divide(result, upper, under, sign)
            if not change:
                break

        if not change:
            break

    pi = merge(result)
    return pi


def by_bernouli(depth=300):
    result = [0 for var in range(depth + 1)]
    import random

    total = 10000
    inner = 0
    for _ in range(total):
        x = random.random()
        y = random.random()
        distance = x * x + y * y
        if distance <= 1:
            inner += 1

    divide(result, inner * 4, total, 1)
    pi = merge(result)
    return pi


def main():
    import time
    start = time.time()
    print(by_arctan(depth=2000))
    print(time.time() - start)
    # print(by_bernouli())


if __name__ == '__main__':
    main()
