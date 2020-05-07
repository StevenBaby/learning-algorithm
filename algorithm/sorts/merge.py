# coding=utf-8
import copy


def sort(data: list, begin=None, end=None):
    if begin is None:
        begin = 0
    if end is None:
        end = len(data) - 1
    if begin >= end:
        return
    length = end - begin + 1
    mid = (end - begin) // 2 + begin

    sort(data, begin, mid)
    sort(data, mid + 1, end)

    temp = [data[var] for var in range(begin, end + 1)]

    # auto list = new int[length]
    # std:: copy(array + begin, array + end + 1, list)

    begin1 = 0
    end1 = mid - begin
    begin2 = end1 + 1
    end2 = length - 1

    index = begin

    while begin1 <= end1 and begin2 <= end2:
        if temp[begin1] < temp[begin2]:
            data[index] = temp[begin1]
            index += 1
            begin1 += 1
        else:
            data[index] = temp[begin2]
            index += 1
            begin2 += 1
    while begin1 <= end1:
        data[index] = temp[begin1]
        index += 1
        begin1 += 1
    while begin2 <= end2:
        data[index] = temp[begin2]
        index += 1
        begin2 += 1


if __name__ == '__main__':
    import random
    data = [random.randint(1, 100) for var in range(32)]
    print(data)
    sort(data)
    print(data)
