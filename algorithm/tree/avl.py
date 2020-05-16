# coding=utf-8

from .binary import SearchNode, SearchTree


class RotateMinxin(object):

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


class AVLNode(SearchNode):

    def factor(self):
        return self.left.height() - self.right.height()


class AVLTree(SearchTree, RotateMinxin):

    Node = AVLNode

    def left_rotate(self, node):
        super().left_rotate(node)
        self.update_height(node)

    def right_rotate(self, node):
        super().right_rotate(node)
        self.update_height(node)

    def rebalance(self, node):
        if abs(node.factor()) < 2:
            return
        if node.factor() == 2:  # left
            if node.left.factor() == 1:  # LL
                self.right_rotate(node)
            elif node.left.factor() == -1:  # LR
                self.left_rotate(node.left)
                self.right_rotate(node)
            elif node.left.factor() == 0:
                self.right_rotate(node)
            else:
                raise Exception(f'factor {node.right.factor()} invalid')
        elif node.factor() == -2:  # right
            if node.right.factor() == 1:  # RL
                self.right_rotate(node.right)
                self.left_rotate(node)
            elif node.right.factor() == -1:  # RR
                self.left_rotate(node)
            elif node.right.factor() == 0:
                self.left_rotate(node)
            else:
                raise Exception(f'factor {node.right.factor()} invalid')
        else:
            raise Exception(f'factor {node.factor()} invalid')

    def insert(self, key):
        node = super().insert(key)

        child = node
        while True:
            parent = child.parent
            if parent == self.nil:
                return parent
            if abs(parent.factor()) >= 2:
                break
            child = parent

        self.rebalance(parent)
        return node

    def delete(self, key):
        node = super().delete(key)

        node.parent_walk(
            callback=lambda e: self.rebalance(e),
            nil=self.nil
        )
