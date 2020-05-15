# coding=utf-8
import unittest

from test_base import BaseTestCase
from algorithm.tree import binary

skip = (__name__ == '__main__')
skip = None


class TestCase(BaseTestCase):

    keys = [7, 4, 11, 3, 6, 9, 18, 2, 14, 19, 12, 17, 22, 20, 21, 10]

    @unittest.skipIf(skip, None)
    def test_build(self):

        tree = binary.SearchTree(self.keys)
        self.assertEqual(tree.height(), 7)

        keys = sorted(self.keys)
        tree = binary.SearchTree(keys)
        self.assertEqual(tree.height(), 16)

        keys = sorted(self.keys)
        tree = binary.SearchTree(keys, random=True)
        self.assertLessEqual(tree.height(), 16)

    @unittest.skipIf(skip, None)
    def test_walk(self):
        tree = binary.SearchTree(self.keys)
        value = []
        tree.inorder_walk(callback=lambda e: value.append(e.key))
        self.assertEqual(value, [2, 3, 4, 6, 7, 9, 10, 11, 12, 14, 17, 18, 19, 20, 21, 22])

        value = []
        tree.preorder_walk(callback=lambda e: value.append(e.key))
        self.assertEqual(value, [7, 4, 3, 2, 6, 11, 9, 10, 18, 14, 12, 17, 19, 22, 20, 21])

        value = []
        tree.postorder_walk(callback=lambda e: value.append(e.key))
        self.assertEqual(value, [2, 3, 6, 4, 10, 9, 12, 17, 14, 21, 20, 22, 19, 18, 11, 7])

    @unittest.skipIf(skip, None)
    def test_search(self):
        tree = binary.SearchTree(self.keys)

        for key in self.keys:
            self.assertTrue(tree.search(key))

        self.assertFalse(tree.search(70))

        minimum = tree.minimum()
        self.assertEqual(minimum.key, 2)

        maximum = tree.maximum()
        self.assertEqual(maximum.key, 22)

        successor = tree.successor(tree.search(7))
        self.assertEqual(successor.key, 9)

        successor = tree.successor(tree.search(6))
        self.assertEqual(successor.key, 7)

        predecessor = tree.predecessor(tree.search(7))
        self.assertEqual(predecessor.key, 6)

        predecessor = tree.predecessor(tree.search(9))
        self.assertEqual(predecessor.key, 7)

    @unittest.skipIf(skip, None)
    def test_delete(self):
        tree = binary.SearchTree(self.keys)

        tree.delete(3)
        self.assertIsNone(tree.search(3))
        tree.delete(4)
        self.assertIsNone(tree.search(4))
        tree.delete(7)
        self.assertIsNone(tree.search(7))

    @unittest.skipIf(skip, None)
    def test_height(self):
        tree = binary.SearchTree(self.keys)
        self.assertEqual(tree.height(), 7)
        tree = binary.SearchTree([1, 2, 3, 4, 5])
        self.assertEqual(tree.height(), 5)


if __name__ == '__main__':
    TestCase.main()
