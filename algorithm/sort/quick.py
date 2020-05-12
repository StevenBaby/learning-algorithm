# coding=utf-8


def quick_sort_version_1(data: list, begin=None, end=None):
    if begin is None:
        begin = 0
    if end is None:
        end = len(data) - 1
    if begin >= end:
        return

    pivot = data[begin]
    left = begin
    right = end

    while left < right:
        while (left < right and data[right] >= pivot):
            right -= 1

        data[left] = data[right]

        while (left < right and data[left] < pivot):
            left += 1

        data[right] = data[left]

    data[left] = pivot
    quick_sort_version_1(data, begin, left - 1)
    quick_sort_version_1(data, left + 1, end)


def quick_sort_version_2(data: list, begin=None, end=None):
    if begin is None:
        begin = 0
    if end is None:
        end = len(data) - 1
    if begin >= end:
        return

    def partion(data, begin, end):
        pivot = data[end]
        i = begin - 1
        for j in range(begin, end):
            if data[j] <= pivot:
                i += 1
                if i == j:
                    continue
                temp = data[i]
                data[i] = data[j]
                data[j] = temp

        # temp = data[i + 1]
        data[end] = data[i + 1]
        data[i + 1] = pivot
        return i + 1

    mid = partion(data, begin, end)
    quick_sort_version_2(data, begin, mid - 1)
    quick_sort_version_2(data, mid + 1, end)
