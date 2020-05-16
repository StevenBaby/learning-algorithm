# coding=utf-8
import unittest

from test_base import BaseTestCase
from algorithm.tree import redblack

skip = (__name__ == '__main__')
skip = None


class TestCase(BaseTestCase):

    @unittest.skipIf(skip, None)
    def test_insert(self):
        tree = redblack.RedBlackTree([11, 2, 14, 1, 7, 15, 5, 8, 4])
        self.assertEqual(tree.root.key, 7)
        self.assertEqual(tree.height(), 4)

        tree = redblack.RedBlackTree()
        for key in [7, 4, 11, 3, 6, 9, 18, 2, 14, 19, 12, 17, 22, 20, 21, 10]:
            tree.insert(key)
        self.assertEqual(tree.root.key, 7)
        self.assertEqual(tree.height(), 5)


if __name__ == '__main__':
    TestCase.main()
