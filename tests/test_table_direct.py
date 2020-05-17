# coding=utf-8
import unittest

from test_base import BaseTestCase
from algorithm.table import direct

skip = (__name__ == '__main__')
skip = None


class TestCase(BaseTestCase):

    keys = [7, 4, 11, 3, 6, 9, 18, 2, 14, 19, 12, 17, 22, 20, 21, 10]

    @unittest.skipIf(skip, None)
    def test_direct_table(self):
        table = direct.DirectAddressTable(size=len(self.keys))
        for index, key in enumerate(self.keys):
            table.insert(index, key)
            self.assertEqual(table.search(index), key)
            self.assertEqual(table.size(), index + 1)

        for index, key in enumerate(self.keys):
            table.delete(index)
            self.assertIsNone(table.search(index))

    @unittest.skipIf(skip, None)
    def test_open_table(self):
        table = direct.OpenAddressTable(size=len(self.keys))
        for index, key in enumerate(self.keys):
            # print(index, key)
            table.insert(key, key)
            self.assertEqual(table.search(key), key)
            self.assertEqual(table.size(), index + 1)

        for key in self.keys:
            table.delete(key)
            self.assertIsNone(table.search(key))

        self.assertEqual(table.size(), 0)


if __name__ == '__main__':
    TestCase.main()
