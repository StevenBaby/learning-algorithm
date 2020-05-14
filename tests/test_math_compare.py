# coding=utf-8

from test_base import BaseTestCase


class TestCase(BaseTestCase):

    def test(self):
        from algorithm.math import compare

        self.assertEqual(compare.max(1, 2, 3, 4, 3, 88, 92, 104, -123), 104)
        self.assertEqual(compare.min(1, 2, 3, 4, 3, 88, 92, 104, -123), -123)
        self.assertEqual(compare.min_max(1, 2, 3, 4, 3, 88, 92, 104, -123), (-123, 104))


if __name__ == '__main__':
    TestCase.main()
