# coding=utf-8


class RedBlackNode(object):

    RED = 0
    BLACK = 1

    def __init__(self, key=None, parent=None, left=None, right=None, color=None):
        self.key = key
        self.parent = parent
        self.left = left
        self.right = right
        self.color = color

    def black_height(self):
        pass


class RedBlackTree(object):

    def __init__(self):
        self.root = None
        self.nil = RedBlackNode(color=RedBlackNode.BLACK)

    def black_height(self):
        # 一棵有n个内部结点的红黑树的高度至多为 2lg(n+1)

        if not self.root:
            return 0
        return self.root.black_height()

    def search(self):
        pass

    def predecessor(self):
        pass

    def successor(self):
        pass

    def minimum(self):
        pass

    def maximum(self):
        pass

    def insert(self):
        pass

    def delete(self):
        pass
