# coding=utf-8

from test_base import BaseTestCase
from algorithm.tree import binary


class TestCase(BaseTestCase):

    keys = [7, 4, 11, 3, 6, 9, 18, 2, 14, 19, 12, 17, 22, 20, 21, 10]

    def test_build(self):

        tree = binary.SearchTree(self.keys)

        nodes = str(tree.get_level_nodes())
        self.assertEqual(tree.height(), 7)
        self.assertEqual(nodes, '[[(None)7], [4(7), (7)11], [3(4), (4)6, 9(11), (11)18], [2(3), (9)10, 14(18), (18)19], [12(14), (14)17, (19)22], [20(22)], [(20)21]]')

        keys = sorted(self.keys)
        tree = binary.SearchTree(keys)
        self.assertEqual(tree.height(), 16)

        keys = sorted(self.keys)
        tree = binary.SearchTree(keys, random=True)
        self.assertLessEqual(tree.height(), 16)

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

    def test_delete(self):
        tree = binary.SearchTree(self.keys)

        tree.delete(3)
        nodes = str(tree.get_level_nodes())
        self.assertEqual(
            nodes,
            '[[(None)7], [4(7), (7)11], [2(4), (4)6, 9(11), (11)18], [(9)10, 14(18), (18)19], [12(14), (14)17, (19)22], [20(22)], [(20)21]]'
        )

        tree.delete(20)
        nodes = str(tree.get_level_nodes())
        self.assertEqual(
            nodes,
            "[[(None)7], [4(7), (7)11], [2(4), (4)6, 9(11), (11)18], [(9)10, 14(18), (18)19], [12(14), (14)17, (19)22], [21(22)]]"
        )

        tree.delete(4)
        self.assertEqual(
            str(tree.get_level_nodes()),
            '[[(None)7], [6(7), (7)11], [2(6), 9(11), (11)18], [(9)10, 14(18), (18)19], [12(14), (14)17, (19)22], [21(22)]]'
        )

        tree.delete(7)
        self.assertEqual(
            str(tree.get_level_nodes()),
            '[[(None)9], [6(9), (9)11], [2(6), 10(11), (11)18], [14(18), (18)19], [12(14), (14)17, (19)22], [21(22)]]'
        )


if __name__ == '__main__':
    TestCase.main()
