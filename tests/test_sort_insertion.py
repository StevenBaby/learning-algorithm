# coding=utf-8

from test_base import BaseTestCase


class TestCase(BaseTestCase):

    def test(self):
        from algorithm.sort import insertion
        from algorithm.sort import generate_random_list
        data = generate_random_list(length=100)
        insertion.insertion_sort(data)
        self.assertEqual(sorted(data), data)


if __name__ == '__main__':
    TestCase.main()
