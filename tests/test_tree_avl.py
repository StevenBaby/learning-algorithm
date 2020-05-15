# coding=utf-8

from test_base import BaseTestCase
from algorithm.tree import avl


class TestCase(BaseTestCase):

    keys = [7, 4, 11, 3, 6, 9, 18, 2, 14, 19, 12, 17, 22, 20, 21, 10]

    def test_insert(self):

        tree = avl.AVLTree()
        for key in [8, 3, 10, 2, 5, 4]:
            tree.insert(key)

        tree = avl.AVLTree()
        for key in [5, 3, 10, 8, 12, 9]:
            tree.insert(key)

        tree = avl.AVLTree()
        for key in range(15):
            tree.insert(key)
        self.assertEqual(tree.height(), 4)


if __name__ == '__main__':
    TestCase.main()
