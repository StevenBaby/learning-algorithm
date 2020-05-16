# coding=utf-8

from .binary import SearchNode, SearchTree
from .avl import RotateMinxin

RED = 0
BLACK = 1


class RedBlackNode(SearchNode):

    def __init__(self, color=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.color = color

    def black_height(self):
        pass

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
    5. For each node, all simple paths from the node to descendant leaves
       contain the same number of black nodes.
    """
    Node = RedBlackNode

    def black_height(self):
        # A red-black tree with n internal nodes has height at most 2 lg(n + 1)

        if not self.root:
            return 0
        return self.root.black_height()

    def insert(self, key):
        node = super().insert(key)
        node.color = RED
        self.insert_fixup(node)
        return node

    def insert_fixup(self, node):
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
                        self.left_rotate(node)
                    node.parent.color = BLACK
                    node.parent.parent.color = RED
                    self.right_rotate(node.parent.parent)
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
                        self.right_rotate(node)
                    node.parent.color = BLACK
                    node.parent.parent.color = RED
                    self.left_rotate(node.parent.parent)

        self.root.color = BLACK

    def transplant(self, node, replace):
        super().transplant(node, replace)
        replace.parent = node.parent

    def delete(self, key):
        # TODO need to finish
        node = self.search(key)
        if not node:
            return None
        if (node.left, node.right) == (self.nil, self.nil):
            replace = node.parent
            self.transplant(node, self.nil)

        elif node.left == self.nil:
            replace = node.right
            self.transplant(node, replace)

        elif node.right == self.nil:
            replace = node.left
            self.transplant(node, replace)

        else:
            replace = self.minimum(node.right)
            if replace.parent != node:
                self.transplant(replace, replace.right)
                replace.right = node.right
                replace.right.parent = replace

            self.transplant(node, replace)
            replace.left = node.left
            replace.left.parent = replace

        node.free()
        return replace
