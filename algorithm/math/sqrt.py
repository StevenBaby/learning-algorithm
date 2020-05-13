# coding=utf-8


def sqrt(number, precision=10, type=str):
    """[compute square root of integer for any precision]

    Arguments:
        number {[int]}

    Keyword Arguments:
        precision {int} -- (default: {10})
        type {type} -- [result type] (default: {'string'})

    Returns:
        if type == str: return string
        if type == int: return int
    """
    # find first bit
    number *= 10000

    high = number
    low = 0

    while high // 10 != low // 10:
        mid = (high + low) // 2
        if mid ** 2 > number:
            high = mid
        else:
            low = mid

    # f(x) = x^2 - number
    # f'(x) = 2x^2
    # x2 = x1 + (-f(x1)) / f'(x1)
    # x2 = x1 + (number - x1^2) / (2(x1)^2)
    # newton method to resolve sqrt

    number //= 100
    result = mid // 10
    bit = 1
    shift = 1
    carry = shift * 10

    distance = number - result ** 2

    for counter in range(1000):
        # distance = number - result ** 2  # optimized by -= operation
        slope = 2 * result

        amend = distance * carry // slope

        number *= carry ** 2  # prepare for next compute
        distance *= carry ** 2

        # (a + b)^2 = a^2 + 2ab + b^2
        # (result + amend)^2 = result^2 + 2 * result * amend + amend^2
        # distance -= 2 * result * amend + amend^2
        distance -= (2 * result * carry + amend) * amend

        result = result * carry + amend

        bit += shift

        if bit == precision:
            break
        if bit * 2 > precision:
            shift = precision - bit
        else:
            shift = bit

        carry = 10 ** shift

    if type == int:
        return result

    result = str(result)
    result = result[:-precision] + "." + result[-precision:]
    return result
