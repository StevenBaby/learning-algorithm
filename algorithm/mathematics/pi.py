# coding=utf-8


def by_arctan(depth=300):

    result = 0
    sign = 1
    for var in range(1, int(depth) * 2, 2):
        result += sign / (var * 2 ** var)
        result += sign / (var * 5 ** var)
        result += sign / (var * 8 ** var)
        sign *= -1

    pi = result * 4
    return pi


def main():
    print(by_arctan())


if __name__ == '__main__':
    main()
