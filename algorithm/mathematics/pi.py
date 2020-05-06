# coding=utf-8


def by_arctan(depth=300):

    def arctan(x, depth):
        if depth < 1:
            return x

        result = 0
        sign = 1
        for var in range(1, int(depth) * 2, 2):
            result += sign * (x ** var) / var
            sign *= -1

        return result

    pi = 4 * (arctan(1 / 2, depth) + arctan(1 / 5, depth) + arctan(1 / 8, depth))
    return pi


def main():
    print(by_arctan())


if __name__ == '__main__':
    main()
