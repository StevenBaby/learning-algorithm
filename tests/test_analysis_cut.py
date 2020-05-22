# coding=utf-8
import unittest

from test_base import BaseTestCase
from algorithm.tree import statistic

skip = (__name__ == '__main__')
skip = None


class TestCase(BaseTestCase):

    @unittest.skipIf(skip, None)
    def test(self):
        price = {
            1: 1,
            2: 5,
            3: 8,
            4: 9,
            5: 10,
            6: 14,
            7: 17,
            8: 20,
            9: 24,
            10: 30,
        }
        from algorithm.analysis import dynamic
        self.assertGreater(dynamic.cut(price, 10), price[10])


if __name__ == '__main__':
    TestCase.main()
