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

    result.insert(1, '.')
    pi = ''.join([str(var) for var in result])
    return pi


def main():
    print(by_arctan(depth=1000))


if __name__ == '__main__':
    main()
