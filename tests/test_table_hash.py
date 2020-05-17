# coding=utf-8
import unittest

from test_base import BaseTestCase
from algorithm.table import hash

skip = (__name__ == '__main__')
skip = None


class TestCase(BaseTestCase):

    keys = [7, 4, 11, 3, 6, 9, 18, 2, 14, 19, 12, 17, 22, 20, 21, 10]

    @unittest.skipIf(skip, None)
    def test_direct_table(self):
        table = hash.DirectAddressTable(size=len(self.keys))
        self.assertEqual(table.size(), 16)
        for index, key in enumerate(self.keys):
            table.insert(index, key)
            self.assertEqual(table.search(index), key)

        for index, key in enumerate(self.keys):
            table.delete(index)
            self.assertIsNone(table.search(index))


if __name__ == '__main__':
    TestCase.main()
