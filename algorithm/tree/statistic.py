# coding=utf-8

from .redblack import RedBlackTree, RedBlackNode


class OrderStatisticNode(RedBlackNode):

    def select(self, index):
        r = self.left.size()
        if index == r:
            return self
        if index < r:
            return self.left.select(index)
        return self.right.select(index - r - 1)


class OrderStatisticTree(RedBlackTree):

    Node = OrderStatisticNode

    def select(self, index):
        return self.root.select(index)

    def rank(self, node):
        r = node.left.size()
        var = node
        while var != self.root:
            if var.is_right():
                r = r + var.parent.left.size() + 1
            var = var.parent
        return r
