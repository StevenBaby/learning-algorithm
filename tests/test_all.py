# coding=utf-8
# coding=utf-8

import unittest
import importlib

modules = [
    'test_math_fact',
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
