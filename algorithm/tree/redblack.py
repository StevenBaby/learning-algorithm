# coding=utf-8

from .binary import SearchNode, SearchTree
from .avl import RotateMinxin

RED = 0
BLACK = 1


class RedBlackNode(SearchNode):

    def __init__(self, color=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.color = color

    def __str__(self):
        if self.color == RED:
            color = 'R'
        else:
            color = 'B'

        return f"[{color}]{super().__str__()}"

    def __repr__(self):
        return self.__str__()


class RedBlackTree(SearchTree, RotateMinxin):
    """ Summary:

    1. Every node is either red or black.
    2. The root is black.
    3. Every leaf (NIL) is black.
    4. If a node is red, then both its children are black.
        (red rode has none red child)
    5. For each node, all simple paths from the node to descendant leaves
       contain the same number of black nodes.
    """
    Node = RedBlackNode

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.nil.color = BLACK

    def _init_node(self, key, data=None):
        node = super()._init_node(key=key, data=data)
        node.color = RED
        return node

    def insert(self, key: int, data=None):
        node = super().insert(key, data=data)
        self._insert_fixup(node)
        return node

    def _insert_fixup(self, node):
        while node.parent.color == RED:
            if node.parent.is_left():
                sibling = node.parent.parent.right
                if sibling.color == RED:
                    node.parent.color = BLACK
                    sibling.color = BLACK
                    node.parent.parent.color = RED
                    node = node.parent.parent
                else:
                    if node.is_right():
                        node = node.parent
                        self._left_rotate(node)
                    node.parent.color = BLACK
                    node.parent.parent.color = RED
                    self._right_rotate(node.parent.parent)
            else:
                sibling = node.parent.parent.left
                if sibling.color == RED:
                    node.parent.color = BLACK
                    sibling.color = BLACK
                    node.parent.parent.color = RED
                    node = node.parent.parent
                else:
                    if node.is_left():
                        node = node.parent
                        self._right_rotate(node)
                    node.parent.color = BLACK
                    node.parent.parent.color = RED
                    self._left_rotate(node.parent.parent)

        self.root.color = BLACK

    def _transplant(self, node, replace):
        super()._transplant(node, replace)
        replace.parent = node.parent

    def delete(self, key):
        node = self.search(key)

        if not node:
            return None

        color = node.color
        middle = node

        if node.left == self.nil:
            replace = node.right
            self._transplant(node, replace)

        elif node.right == self.nil:
            replace = node.left
            self._transplant(node, replace)

        else:
            middle = self.minimum(node.right)
            color = middle.color
            replace = middle.right

            if middle.parent == node:
                replace.parent = middle
            else:
                self._transplant(middle, replace)
                middle.right = node.right
                middle.right.parent = middle

            self._transplant(node, middle)
            middle.left = node.left
            middle.left.parent = middle
            middle.color = node.color

        if color == BLACK:
            self._delete_fixup(replace)

        node.free()
        return replace

    def _delete_fixup(self, node):
        while node != self.root and node.color == BLACK:
            if node.is_left():
                sibling = node.parent.right
                if sibling.color == RED:
                    sibling.color = BLACK
                    node.parent.color = RED
                    self._left_rotate(node.parent)
                    node = node.parent.right
                if sibling.left.color == BLACK and sibling.right.color == BLACK:
                    sibling.color = RED
                    node = node.parent
                else:
                    if sibling.right.color == BLACK:
                        sibling.left.color = BLACK
                        sibling.color = RED
                        self._right_rotate(sibling)
                        sibling = node.parent.right
                    sibling.color = node.parent.color
                    node.parent.color = BLACK
                    node.right.color = BLACK
                    self._right_rotate(node.parent)
                    node = self.root
            else:
                sibling = node.parent.left
                if sibling.color == RED:
                    sibling.color = BLACK
                    node.parent.color = RED
                    self._right_rotate(node.parent)
                    node = node.parent.left
                if sibling.right.color == BLACK and sibling.left.color == BLACK:
                    sibling.color = RED
                    node = node.parent
                else:
                    if sibling.left.color == BLACK:
                        sibling.right.color = BLACK
                        sibling.color = RED
                        self._left_rotate(sibling)
                        sibling = node.parent.left
                    sibling.color = node.parent.color
                    node.parent.color = BLACK
                    node.left.color = BLACK
                    self._left_rotate(node.parent)
                    node = self.root
        node.color = BLACK
