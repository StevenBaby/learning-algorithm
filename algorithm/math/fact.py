# coding=utf-8
"""
阶乘
"""


def fact(number, result=1):
    """[阶乘尾递归求解算法]
    """
    if number <= 1:
        return result

    return fact(number=number - 1, result=result * number)
