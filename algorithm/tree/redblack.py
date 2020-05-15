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

    def __str__(self):
        if self.color == self.RED:
            color = 'R'
        else:
            color = 'B'

        return f"[{color}]{self.key}({self.parent.key or ''})"

    def __repr__(self):
        return self.__str__()


class RedBlackTree(object):

    def __init__(self):
        self.nil = RedBlackNode(color=RedBlackNode.BLACK)
        self.root = self.nil

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

    def insert(self, key):
        node = RedBlackNode(key=key, left=self.nil, right=self.nil, color=RedBlackNode.RED)
        parent = self.nil
        child = self.root

        while child != self.nil:
            parent = child
            if node.key < child.key:
                child = child.left
            else:
                child = child.right

        node.parent = parent

        if parent == self.nil:
            self.root = node
        elif node.key < parent.key:
            parent.left = node
        else:
            parent.right = node
        self._insert_fixup(node)

    def _insert_fixup(self, node):
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
        pass

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

    def _right_rotate(self, node):

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

    def get_levels(self):
        queue = [(self.root, 1)]
        levels = {}

        while queue:
            node, level = queue.pop()
            if node == self.nil:
                continue
            levels.setdefault(level, [])
            levels[level].append(node)

            queue.insert(0, (node.left, level + 1))
            queue.insert(0, (node.right, level + 1))

        levels = sorted(levels.items(), key=lambda e: e[0])
        levels = [level for var, level in levels]
        return levels
