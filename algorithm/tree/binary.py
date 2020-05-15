

class ArrayBinaryTree(list):

    def __init__(self):
        super().__init__()

    def size(self):
        return len(self)

    @staticmethod
    def parent(index):
        return (index - 1) // 2

    @staticmethod
    def left(index):
        return index * 2 + 1

    @staticmethod
    def right(index):
        return index * 2 + 2


class BinaryNode(object):

    ROOT = 1
    LEFT = 2
    RIGHT = 3

    def __init__(self, key=None, parent=None, left=None, right=None):
        self.key = key
        self.parent = parent
        self.left = left
        self.right = right

    def relation(self):
        if not self.parent:
            return self.ROOT
        if self.parent.left == self:
            return self.LEFT
        else:
            return self.RIGHT

    def __str__(self):
        parent = None
        if self.parent:
            parent = self.parent.key

        rel = self.relation()
        if rel == self.ROOT:
            return f"{self.key}"
        elif rel == self.LEFT:
            return f"{self.key}({parent})"
        else:
            return f"({parent}){self.key}"

    def __repr__(self):
        return self.__str__()


class BinaryTree(object):

    Node = BinaryNode

    def __init__(self):
        self.nil = self.Node()
        self.root = self.nil

    def insert(self, key):
        pass

    def delete(self, key):
        pass

    def get_level_nodes(self):
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


class SearchNode(BinaryNode):

    def inorder_walk(self, callback=print, nil=None):
        if self.left != nil:
            self.left.inorder_walk(callback, nil)
        callback(self)
        if self.right != nil:
            self.right.inorder_walk(callback, nil)

    def preorder_walk(self, callback=print, nil=None):
        callback(self)
        if self.left != nil:
            self.left.preorder_walk(callback, nil)
        if self.right != nil:
            self.right.preorder_walk(callback, nil)

    def postorder_walk(self, callback=print, nil=None):
        if self.left != nil:
            self.left.postorder_walk(callback, nil)
        if self.right != nil:
            self.right.postorder_walk(callback, nil)
        callback(self)


class SearchTree(BinaryTree):

    Node = SearchNode

    def search(self, key):
        node = self.root
        while node != self.nil:
            if node.key == key:
                return node
            if key < node.key:
                node = node.left
            else:
                node = node.right
        return None

    def maximum(self, node=None):
        if node is None:
            node = self.root
        if node == self.nil:
            return None
        while node.right != self.nil:
            node = node.right
        return node

    def minimum(self, node=None):
        if node is None:
            node = self.root
        if node == self.nil:
            return None
        while node.left != self.nil:
            node = node.left
        return node

    def successor(self, node):
        if node.right != self.nil:
            return self.minimum(node.right)
        parent = node.parent
        while parent != self.nil and node == parent.right:
            node = parent
            parent = node.parent

        if parent == self.nil:
            return None
        return parent

    def inorder_walk(self, callback=print):
        self.root.inorder_walk(callback, self.nil)

    def preorder_walk(self, callback=print):
        self.root.preorder_walk(callback, self.nil)

    def postorder_walk(self, callback=print):
        self.root.postorder_walk(callback, self.nil)

    def insert(self, key):
        node = self.Node(key=key, left=self.nil, right=self.nil)

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
