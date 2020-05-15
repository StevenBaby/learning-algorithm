# coding=utf-8

from .binary import SearchNode, SearchTree


class AVLNode(SearchNode):

    def factor(self):
        return abs(self.left.height() - self.right.height())


class AVLTree(SearchTree):

    Node = AVLNode

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.nil._height = 0

    def left_rotate(self, node):

        x = node
        y = x.right

        parent = x.parent
        beta = y.left

        x.right = beta
        if beta != self.nil:
            beta.parent = x

        y.parent = parent
        if parent == self.nil:
            self.root = y
        elif x == parent.left:
            parent.left = y
        else:
            parent.right = y

        y.left = x
        x.parent = y

    def right_rotate(self, node):

        y = node
        x = y.right

        parent = y.parent
        beta = x.right

        y.left = beta
        if beta != self.nil:
            beta.parent = y

        x.parent = parent
        if parent == self.nil:
            self.root = x
        elif y == parent.left:
            parent.left = x
        else:
            parent.right = x

        x.right = y
        y.parent = x

    def insert(self, key):
        node = super().insert(key)

        parent = node.parent
        child = node
        while parent != self.nil and parent.factor() <= 1:
            child = parent
            parent = parent.parent

        if parent == self.nil:
            return node

        if child.is_left():
            self.right_rotate(parent)
        else:
            self.left_rotate(parent)

        return node
