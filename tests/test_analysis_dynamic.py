# coding=utf-8
import unittest

from test_base import BaseTestCase

skip = (__name__ == '__main__')
skip = None


class TestCase(BaseTestCase):

    @unittest.skipIf(skip, None)
    def test(self):
        pass


if __name__ == '__main__':
    TestCase.main()
