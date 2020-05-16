# coding=utf-8

from .binary import SearchNode, SearchTree
from .avl import RotateMinxin


class RedBlackNode(SearchNode):

    RED = 0
    BLACK = 1

    def __init__(self, color=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.color = color

    def black_height(self):
        pass

    def __str__(self):
        if self.color == self.RED:
            color = 'R'
        else:
            color = 'B'

        return f"[{color}]{super()__str__()}"

    def __repr__(self):
        return self.__str__()


class RedBlackTree(SearchTree, RotateMinxin):

    Node = RedBlackNode

    def black_height(self):
        # 一棵有n个内部结点的红黑树的高度至多为 2lg(n+1)

        if not self.root:
            return 0
        return self.root.black_height()

    def insert(self, key):
        node = super().insert(key)
        node.color = RedBlackNode.RED
        self.insert_fixup(node)

    def insert_fixup(self, node):
        while node.parent.color == RedBlackNode.RED:
            if node.parent == node.parent.parent.left:
                y = node.parent.parent.right
                if y.color == RedBlackNode.RED:
                    node.parent.color = RedBlackNode.BLACK
                    y.color = RedBlackNode.BLACK
                    node.parent.parent.color = RedBlackNode.RED
                    node = node.parent.parent
                elif node == node.p.right:
                    node = node.parent
                    self._left_rotate(node)
                node.parent.color = RedBlackNode.BLACK
                node.parent.parent.color = RedBlackNode.RED
                self._right_rotate(node.parent.parent)
            else:
                y = node.parent.parent.left
                if y.color == RedBlackNode.RED:
                    node.parent.color = RedBlackNode.BLACK
                    y.color = RedBlackNode.BLACK
                    node.parent.parent.color = RedBlackNode.RED
                    node = node.parent.parent
                elif node == node.p.left:
                    node = node.parent
                    self._right_rotate(node)
                node.parent.color = RedBlackNode.BLACK
                node.parent.parent.color = RedBlackNode.RED
                self._left_rotate(node.parent.parent)
            self.root.color = RedBlackNode.BLACK

    def delete(self):
        node = super().delete(self)

    def left_rotate(self, node):
        super().left_rotate(node)

    def right_rotate(self, node):
        super().right_rotate(node)
