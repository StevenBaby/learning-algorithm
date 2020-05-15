# coding=utf-8

from test_base import BaseTestCase


class TestCase(BaseTestCase):

    def test(self):
        from algorithm.tree import redblack

        tree = redblack.RedBlackTree()


if __name__ == '__main__':
    TestCase.main()
