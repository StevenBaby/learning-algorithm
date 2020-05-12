# coding=utf-8

from test_base import BaseTestCase


class TestCase(BaseTestCase):

    def test(self):
        from algorithm.sort import quick
        from algorithm.sort import generate_random_list
        data = generate_random_list(length=100)
        quick.quick_sort_version_1(data)
        self.assertEqual(sorted(data), data)

        data = generate_random_list(length=1000)
        quick.quick_sort_version_2(data)
        self.assertEqual(sorted(data), data)


if __name__ == '__main__':
    TestCase.main()
