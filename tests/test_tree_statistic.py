# coding=utf-8
import unittest

from test_base import BaseTestCase
from algorithm.tree import statistic

skip = (__name__ == '__main__')
skip = None


class TestCase(BaseTestCase):

    @unittest.skipIf(skip, None)
    def test_search(self):
        keys = [7, 4, 11, 3, 6, 9, 18, 2, 14, 19, 12, 17, 22, 20, 21, 10]
        tree = statistic.OrderStatisticTree(keys)

        node = tree.select(0)
        self.assertEqual(node.key, 2)
        self.assertEqual(tree.rank(node), 0)

        node = tree.select(15)
        self.assertEqual(node.key, 22)
        self.assertEqual(tree.rank(node), 15)

        node = tree.select(8)
        self.assertEqual(node.key, 12)
        self.assertEqual(tree.rank(node), 8)


if __name__ == '__main__':
    TestCase.main()
