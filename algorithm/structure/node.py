# coding=utf-8


class Node(object):

    def __init__(self, value=None):
        self.value = value

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return self.__str__()


class BNode(Node):

    def __init__(self, parent=None, left=None, right=None):
        self.parent = parent
        self.left = left
        self.right = right
        self.value = None
