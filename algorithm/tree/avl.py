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

        self.update_height(node)

    def right_rotate(self, node):

        y = node
        x = y.left

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

        self.update_height(node)

    def insert(self, key):
        node = super().insert(key)

        child = node
        pattern = []

        while True:
            parent = child.parent
            if parent == self.nil:
                return node

            pattern.append(child.relation())

            if parent.factor() >= 2:
                break
            child = parent

        pattern = pattern[-2:]

        if pattern == [self.Node.RIGHT, self.Node.RIGHT]:
            self.left_rotate(parent)
        elif pattern == [self.Node.LEFT, self.Node.LEFT]:
            self.right_rotate(parent)
        elif pattern == [self.Node.LEFT, self.Node.RIGHT]:
            self.right_rotate(child)
            self.left_rotate(parent)
        elif pattern == [self.Node.RIGHT, self.Node.LEFT]:
            self.left_rotate(child)
            self.right_rotate(parent)

        return node
