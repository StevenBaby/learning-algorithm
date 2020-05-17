# coding=utf-8
import unittest

from test_base import BaseTestCase
from algorithm.table import hash

skip = (__name__ == '__main__')
skip = None


class TestCase(BaseTestCase):

    keys = [7, 4, 11, 3, 6, 9, 18, 2, 14, 19, 12, 17, 22, 20, 21, 10]

    @unittest.skipIf(skip, None)
    def test(self):
        table = hash.ChainHashTable()


if __name__ == '__main__':
    TestCase.main()
