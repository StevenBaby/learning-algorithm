# coding=utf-8

from test_base import BaseTestCase


class TestCase(BaseTestCase):

    def test(self):
        from algorithm.math import pi
        self.maxDiff = None
        self.assertEqual(int(pi.bernouli()), 3)

        PI = '3.141592653589793238462643383279'
        self.assertEqual(pi.chudnovsky(precision=30), PI)

        PI = '3.14159265358979323846264338327950288419716939937510582097494459230781640628620899'
        self.assertEqual(pi.chudnovsky(precision=80), PI)


if __name__ == '__main__':
    TestCase.main()
