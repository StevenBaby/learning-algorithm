# coding=utf-8
import unittest

from test_base import BaseTestCase
from algorithm.table.queue import Queue

skip = (__name__ == '__main__')
skip = None


class TestCase(BaseTestCase):

    keys = [7, 4, 11, 3, 6, 9, 18, 2, 14, 19, 12, 17, 22, 20, 21, 10]

    @unittest.skipIf(skip, None)
    def test(self):
        queue = Queue()
        for key in self.keys:
            queue.push(key)

        for key in self.keys:
            node = queue.pop()
            self.assertEqual(node, key)
        self.assertTrue(queue.empty())


if __name__ == '__main__':
    TestCase.main()
