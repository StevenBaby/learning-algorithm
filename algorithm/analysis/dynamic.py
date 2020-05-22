# coding=utf-8


def cut(price, n):
    if n == 0:
        return 0
    max_price = -float("inf")
    for var in range(1, n + 1):
        max_price = max(max_price, price[var] + cut(price, n - 1))
    return max_price
