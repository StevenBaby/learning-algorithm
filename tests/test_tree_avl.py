# coding=utf-8
import unittest

from test_base import BaseTestCase
from algorithm.tree import avl

skip = (__name__ == '__main__')
skip = None


class TestCase(BaseTestCase):

    keys = [7, 4, 11, 3, 6, 9, 18, 2, 14, 19, 12, 17, 22, 20, 21, 10]

    @unittest.skipIf(skip, None)
    def test_search(self):
        tree = avl.AVLTree(self.keys)

        for key in self.keys:
            self.assertTrue(tree.search(key))

        self.assertFalse(tree.search(70))

        minimum = tree.minimum()
        self.assertEqual(minimum.key, 2)

        maximum = tree.maximum()
        self.assertEqual(maximum.key, 22)


    @unittest.skipIf(skip, None)
    def test_insert(self):
        tree = avl.AVLTree()
        for key in [8, 7, 6, 5, 4]:
            tree.insert(key)
            # print(tree.height())
            # tree.print_level_nodes()
            tree.inorder_walk(callback=lambda e: abs(e._factor()) < 2)

        self.assertEqual(tree.root.key, 7)
        self.assertEqual(tree.height(), 3)

        tree = avl.AVLTree()
        for key in [4, 5, 6, 7, 8]:
            tree.insert(key)
            # print(tree.height())
            # tree.print_level_nodes()
            tree.inorder_walk(callback=lambda e: abs(e._factor()) < 2)

        self.assertEqual(tree.root.key, 5)
        self.assertEqual(tree.height(), 3)

        tree = avl.AVLTree()
        for key in [8, 3, 10, 2, 5, 4]:
            tree.insert(key)
            tree.inorder_walk(callback=lambda e: abs(e._factor()) < 2)
            # print(tree.height())
            # print(tree.get_level_nodes())

        self.assertEqual(tree.root.key, 5)
        self.assertEqual(tree.height(), 3)

        tree = avl.AVLTree()
        for key in [5, 3, 10, 8, 12, 9]:
            tree.insert(key)
            tree.inorder_walk(callback=lambda e: abs(e._factor()) < 2)
        self.assertEqual(tree.root.key, 8)
        self.assertEqual(tree.height(), 3)

        tree = avl.AVLTree()
        for key in range(1, 16):
            tree.insert(key)
            tree.inorder_walk(callback=lambda e: abs(e._factor()) < 2)

        self.assertEqual(tree.height(), 4)

    @unittest.skipIf(skip, None)
    def test_delete(self):
        tree = avl.AVLTree([20, 10, 30, 5, 15])
        tree.delete(30)
        self.assertEqual(tree.root.key, 10)

        tree = avl.AVLTree([50, 40, 60, 30, 45, 55, 10])
        tree.delete(55)
        self.assertEqual(tree.root.key, 40)

        tree = avl.AVLTree([50, 40, 60, 45])
        tree.delete(60)
        self.assertEqual(tree.root.key, 45)


if __name__ == '__main__':
    TestCase.main()
