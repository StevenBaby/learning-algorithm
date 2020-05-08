

def sqrt(value):
    # x^2 - value = 0
    # f(x) = x^2 - value
    # newton method to resolve sqrt

    # slope = 2 * x

    x = 1
    for _ in range(10):
        x = x - (x * x - value) / (2 * x)
    return x


if __name__ == '__main__':
    print(sqrt(2))
