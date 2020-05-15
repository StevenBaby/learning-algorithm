# coding=utf-8

from test_base import BaseTestCase
from algorithm.tree import avl


class TestCase(BaseTestCase):

    keys = [7, 4, 11, 3, 6, 9, 18, 2, 14, 19, 12, 17, 22, 20, 21, 10]

    def test(self):

        tree = avl.AVLTree()
        for key in [1, 2, 3, 4, 5, 6]:
            tree.insert(key)
            print(tree.get_level_nodes())


if __name__ == '__main__':
    TestCase.main()
