# coding=utf-8

from test_base import BaseTestCase


class TestCase(BaseTestCase):

    def test(self):
        from algorithm.math import sqrt

        self.assertEqual(sqrt.sqrt(2), '1.4142135623')
        self.assertEqual(sqrt.sqrt(2, precision=31), '1.4142135623730950488016887242096')
        self.assertEqual(sqrt.sqrt(3456), '58.7877538267')

        self.assertEqual(sqrt.sqrt(2, type=int), 14142135623)
        self.assertEqual(sqrt.sqrt(4, type=int), 20000000000)


if __name__ == '__main__':
    TestCase.main()
