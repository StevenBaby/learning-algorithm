# coding=utf-8
import unittest

from test_base import BaseTestCase
from algorithm.linear import list as linear

skip = (__name__ == '__main__')
skip = None


class TestCase(BaseTestCase):

    keys = [7, 4, 11, 3, 6, 9, 18, 2, 14, 19, 12, 17, 22, 20, 21, 10]

    @unittest.skipIf(skip, None)
    def test_append(self):
        list = linear.LinkedList()
        for key in self.keys:
            list.append(key)
            self.assertEqual(list.size(), 1)
            self.assertEqual(list.pop().data, key)
            self.assertEqual(list.size(), 0)

    @unittest.skipIf(skip, None)
    def test_search(self):
        list = linear.LinkedList(self.keys)
        self.assertEqual(list.search(22).data, 22)
        self.assertIsNone(list.search(100))

    @unittest.skipIf(skip, None)
    def test_insert(self):
        list = linear.LinkedList()
        for key in self.keys:
            list.insert(0, key)
        self.assertEqual(list.size(), 16)
        for key in self.keys:
            self.assertEqual(list.pop().data, key)

    @unittest.skipIf(skip, None)
    def test_delete(self):
        list = linear.LinkedList(self.keys)
        self.assertFalse(list.empty())
        for index, key in enumerate(self.keys):
            list.delete(key)
            self.assertEqual(list.size(), len(self.keys) - index - 1)
        self.assertTrue(list.empty())


if __name__ == '__main__':
    TestCase.main()
