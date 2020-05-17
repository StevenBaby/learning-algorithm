# coding=utf-8
import unittest

from test_base import BaseTestCase
from algorithm.table import lists

skip = (__name__ == '__main__')
skip = None


class TestCase(BaseTestCase):

    keys = [7, 4, 11, 3, 6, 9, 18, 2, 14, 19, 12, 17, 22, 20, 21, 10]

    @unittest.skipIf(skip, None)
    def test_append(self):
        list = lists.LinkedList()
        for key in self.keys:
            list.append(key)
            self.assertEqual(list.size(), 1)
            self.assertEqual(list.pop().data, key)
            self.assertEqual(list.size(), 0)

    @unittest.skipIf(skip, None)
    def test_search(self):
        list = lists.LinkedList(self.keys)
        self.assertEqual(list.search(22).data, 22)
        self.assertIsNone(list.search(100))

    @unittest.skipIf(skip, None)
    def test_insert(self):
        list = lists.LinkedList()
        for key in self.keys:
            list.insert(0, key)
        self.assertEqual(list.size(), 16)
        for key in self.keys:
            self.assertEqual(list.pop().data, key)

    @unittest.skipIf(skip, None)
    def test_delete(self):
        list = lists.LinkedList(self.keys)
        self.assertFalse(list.empty())
        for index, key in enumerate(self.keys):
            list.delete(key)
            self.assertEqual(list.size(), len(self.keys) - index - 1)
        self.assertTrue(list.empty())

    @unittest.skipIf(skip, None)
    def test_circular_list(self):
        list = lists.CircularList()
        for data in self.keys:
            list.append(data)
        list.print_list()
        list.walk(
            callback=lambda e: None,
            stop=lambda index, node: self.assertEqual(node.data, self.keys[index])
        )
        self.assertEqual(list.head.prev.data, 10)
        self.assertEqual(list.size(), 16)
        self.assertEqual(list.search(21).data, 21)
        self.assertEqual(list.get(14).data, 21)
        self.assertIsNone(list.search(123))
        list.insert(5, 66)
        self.assertEqual(list.get(5).data, 66)
        self.assertEqual(list.get(6).data, 9)
        list.delete(7)
        self.assertEqual(list.head.data, 4)
        list.delete(10)
        self.assertEqual(list.head.prev.data, 21)


if __name__ == '__main__':
    TestCase.main()
