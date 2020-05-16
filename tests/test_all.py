# coding=utf-8
# coding=utf-8

import unittest
import importlib

modules = [
    'test_math_fact',
    'test_math_sqrt',
    'test_math_pi',

    'test_linear_list',
    'test_linear_steak',
    'test_linear_queue',

    'test_tree_heap',
    'test_tree_binary',
    'test_tree_avl',

    'test_sort_insertion',
    'test_sort_quick',
]


def main():
    suite = unittest.TestSuite()
    for name in modules:
        module = importlib.import_module(name)
        suite.addTest(unittest.makeSuite(module.TestCase))

    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == '__main__':
    main()
