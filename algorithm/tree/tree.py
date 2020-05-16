# coding=utf-8


class BaseNode(object):

    pass


class Tree(object):

    Node = BaseNode

    def __init__(self):
        self.nil = self.Node()
        self.root = self.nil


class SiblingNode(BaseNode):

    def __init__(self, data, parent=None, child=None, sibling=None):
        self.data = data
        self.parent = None
        self.child = None
        self.sibling = None


class SiblingTree(Tree):

    Node = SiblingNode
