# coding=utf-8

import os
import sys
import unittest

dirname = os.path.dirname(os.path.abspath(__file__))
project = os.path.dirname(dirname)
if project not in sys.path:
    sys.path.insert(0, project)


class BaseTestCase(unittest.TestCase):

    @staticmethod
    def main():
        return unittest.main(failfast=True)
