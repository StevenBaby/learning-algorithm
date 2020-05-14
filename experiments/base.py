# coding=utf-8

import os
import sys

dirname = os.path.dirname(os.path.abspath(__file__))
project = os.path.dirname(dirname)
if project not in sys.path:
    sys.path.insert(0, project)
