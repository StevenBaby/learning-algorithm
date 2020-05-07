# coding=utf-8


def sort(data: list):
    for j in range(1, len(data)):
        key = data[j]
        i = j - 1
        while i >= 0 and data[i] > key:
            data[i + 1] = data[i]
            i -= 1
        data[i + 1] = key


if __name__ == '__main__':
    import random
    data = [random.randint(1, 100) for var in range(32)]
    print(data)
    sort(data)
    print(data)
