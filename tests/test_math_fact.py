# coding=utf-8

from test_base import BaseTestCase


class TestCase(BaseTestCase):

    def test_fact(self):
        from algorithm.math import fact

        self.assertEqual(fact.fact(5), 120)
        self.assertEqual(fact.fact(6), 720)


if __name__ == '__main__':
    TestCase.main()
