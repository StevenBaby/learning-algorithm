# coding=utf-8

from test_base import BaseTestCase


class TestCase(BaseTestCase):

    def test(self):
        from algorithm.tree import binary

        keys = [7, 4, 11, 3, 6, 9, 18, 2, 14, 19, 12, 17, 22, 20]

        tree = binary.SearchTree()
        for key in keys:
            tree.insert(key)

        value = []
        tree.inorder_walk(callback=lambda e: value.append(e.key))
        print(value)
        self.assertEqual(value, [2, 3, 4, 6, 7, 9, 11, 12, 14, 17, 18, 19, 20, 22])


if __name__ == '__main__':
    TestCase.main()
