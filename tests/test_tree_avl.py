# coding=utf-8

from test_base import BaseTestCase


class TestCase(BaseTestCase):

    def test(self):
        from algorithm.tree import avl

        # keys = [7, 4, 11, 3, 6, 9, 18, 2, 14, 19, 12, 17, 22, 20]
        keys = [2, 3, 4, 6, 7, 9, 11, 12, 14, 17, 18, 19, 20, 22]

        tree = avl.AVLTree()
        for key in keys:
            tree.insert(key)
            print(tree.get_level_nodes())


if __name__ == '__main__':
    TestCase.main()
