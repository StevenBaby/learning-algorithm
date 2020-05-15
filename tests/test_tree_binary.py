# coding=utf-8

from test_base import BaseTestCase


class TestCase(BaseTestCase):

    keys = [7, 4, 11, 3, 6, 9, 18, 2, 14, 19, 12, 17, 22, 20]

    def test_search_tree(self):
        from algorithm.tree import binary

        tree = binary.SearchTree()
        for key in self.keys:
            tree.insert(key)

        nodes = str(tree.get_level_nodes())
        self.assertEqual(nodes, '[[(None)7], [4(7), (7)11], [3(4), (4)6, 9(11), (11)18], [2(3), 14(18), (18)19], [12(14), (14)17, (19)22], [20(22)]]')

        value = []
        tree.inorder_walk(callback=lambda e: value.append(e.key))
        self.assertEqual(value, [2, 3, 4, 6, 7, 9, 11, 12, 14, 17, 18, 19, 20, 22])

        value = []
        tree.preorder_walk(callback=lambda e: value.append(e.key))
        self.assertEqual(value, [7, 4, 3, 2, 6, 11, 9, 18, 14, 12, 17, 19, 22, 20])

        value = []
        tree.postorder_walk(callback=lambda e: value.append(e.key))
        self.assertEqual(value, [2, 3, 6, 4, 9, 12, 17, 14, 20, 22, 19, 18, 11, 7])

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

if __name__ == '__main__':
    TestCase.main()
