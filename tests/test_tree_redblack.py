# coding=utf-8
import unittest

from test_base import BaseTestCase
from algorithm.tree import redblack

skip = (__name__ == '__main__')
skip = None


class TestCase(BaseTestCase):

    @unittest.skipIf(skip, None)
    def test_search(self):
        keys = [7, 4, 11, 3, 6, 9, 18, 2, 14, 19, 12, 17, 22, 20, 21, 10]
        tree = redblack.RedBlackTree(keys)

        for key in keys:
            self.assertTrue(tree.search(key))

        self.assertFalse(tree.search(70))

        minimum = tree.minimum()
        self.assertEqual(minimum.key, 2)

        maximum = tree.maximum()
        self.assertEqual(maximum.key, 22)

    @unittest.skipIf(skip, None)
    def test_insert(self):
        levels = {
            7: [7],
            14: [7, 14],
            11: [11, 7, 14],
            3: [11, 7, 14, 3],
            6: [11, 6, 14, 3, 7],
            9: [11, 6, 14, 3, 7, 9],
            10: [11, 6, 14, 3, 9, 7, 10],
            18: [11, 6, 14, 3, 9, 18, 7, 10],
            2: [11, 6, 14, 3, 9, 18, 2, 7, 10],
            4: [11, 6, 14, 3, 9, 18, 2, 4, 7, 10],
            19: [11, 6, 18, 3, 9, 14, 19, 2, 4, 7, 10],
            12: [11, 6, 18, 3, 9, 14, 19, 2, 4, 7, 10, 12],
            17: [11, 6, 18, 3, 9, 14, 19, 2, 4, 7, 10, 12, 17],
            22: [11, 6, 18, 3, 9, 14, 19, 2, 4, 7, 10, 12, 17, 22],
            20: [11, 6, 18, 3, 9, 14, 20, 2, 4, 7, 10, 12, 17, 19, 22],
            21: [11, 6, 18, 3, 9, 14, 20, 2, 4, 7, 10, 12, 17, 19, 22, 21],
        }
        tree = redblack.RedBlackTree()

        for key in levels.keys():
            tree.insert(key)
            self.assertEqual(tree.level_key_list(), levels[key])

        self.assertEqual(tree.root.key, 11)
        self.assertEqual(tree.height(), 5)

    @unittest.skipIf(skip, None)
    def test_delete(self):
        tree = redblack.RedBlackTree([7, 14, 11, 3, 6, 9, 10, 18, 2, 4, 19, 12, 17, 22, 20, 21])
        self.assertEqual(tree.root.key, 11)
        self.assertEqual(tree.height(), 5)

        keys = {
            22: [11, 6, 18, 3, 9, 14, 20, 2, 4, 7, 10, 12, 17, 19, 21],
            9: [11, 6, 18, 3, 10, 14, 20, 2, 4, 7, 12, 17, 19, 21],
            11: [12, 6, 18, 3, 10, 14, 20, 2, 4, 7, 17, 19, 21],
            12: [14, 6, 18, 3, 10, 17, 20, 2, 4, 7, 19, 21],
        }
        for key in keys.keys():
            tree.delete(key)
            self.assertEqual(tree.level_key_list(), keys[key])


if __name__ == '__main__':
    TestCase.main()
