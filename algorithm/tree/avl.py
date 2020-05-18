# coding=utf-8

from .binary import SearchNode, SearchTree


class RotateMinxin(object):

    def _left_rotate(self, node):

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

        self._update_height(node)
        self._update_size(node)

    def _right_rotate(self, node):

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

        self._update_height(node)
        self._update_size(node)


class AVLNode(SearchNode):

    def _factor(self):
        return self.left.height() - self.right.height()


class AVLTree(SearchTree, RotateMinxin):

    Node = AVLNode

    def _rebalance(self, node):
        if abs(node._factor()) < 2:
            return
        if node._factor() == 2:  # left
            if node.left._factor() == 1:  # LL
                self._right_rotate(node)
            elif node.left._factor() == -1:  # LR
                self._left_rotate(node.left)
                self._right_rotate(node)
            elif node.left._factor() == 0:
                self._right_rotate(node)
            else:
                raise Exception(f'factor {node.right._factor()} invalid')
        elif node._factor() == -2:  # right
            if node.right._factor() == 1:  # RL
                self._right_rotate(node.right)
                self._left_rotate(node)
            elif node.right._factor() == -1:  # RR
                self._left_rotate(node)
            elif node.right._factor() == 0:
                self._left_rotate(node)
            else:
                raise Exception(f'factor {node.right._factor()} invalid')
        else:
            raise Exception(f'factor {node._factor()} invalid')

    def insert(self, key, data=None):
        node = super().insert(key, data=data)

        child = node
        while True:
            parent = child.parent
            if parent == self.nil:
                return parent
            if abs(parent._factor()) >= 2:
                break
            child = parent

        self._rebalance(parent)
        return node

    def delete(self, key):
        node = super().delete(key)

        node.parent_walk(
            callback=lambda e: self._rebalance(e),
            nil=self.nil
        )
