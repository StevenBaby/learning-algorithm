

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

    def __init__(self, key=None, data=None, parent=None, left=None, right=None, height=0):
        self.key = key
        self.data = data
        self.parent = parent
        self.left = left
        self.right = right
        self._height = height

    def relation(self):
        if not self.parent:
            return self.ROOT
        if self.parent.left == self:
            return self.LEFT
        else:
            return self.RIGHT

    def is_left(self):
        return self.LEFT == self.relation()

    def is_right(self):
        return self.RIGHT == self.relation()

    def free(self):
        self.key = None
        self.data = None
        self.parent = None
        self.left = None
        self.right = None

    def __str__(self):
        if self.key is None:
            return 'nil'
        parent = 'nil'
        if self.parent and self.parent.key is not None:
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

    def height(self):
        if self._height > 0:
            return self._height
        return self._reckon_height()

    def _reckon_height(self):
        height = 0
        if self.left:
            height = max(self.left.height() + 1, height)
        if self.right:
            height = max(self.right.height() + 1, height)
        return height

    def _update_height(self):
        self._height = self._reckon_height()
        return self._height

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

    def levelorder_walk(self, callback=print, nil=None):
        from ..linear.queue import Queue
        queue = Queue([self])

        while not queue.empty():
            node = queue.pop()
            if node == nil:
                continue
            callback(node)
            queue.push(node.left)
            queue.push(node.right)

    def parent_walk(self, callback=print, nil=None):
        node = self
        while node != nil:
            callback(node)
            node = node.parent


class BinaryTree(object):

    Node = BinaryNode

    def __init__(self):
        self.nil = self.Node()
        self.root = self.nil
        self._size = 0

    def _init_node(self, key, data=None):
        node = self.Node(key=key, data=data, left=self.nil, right=self.nil, height=1)
        return node

    def height(self):
        return self.root.height()

    def size(self):
        return self._size

    def get_level_nodes(self):
        from ..linear.queue import Queue
        queue = Queue([(self.root, 1)])
        levels = {}

        while not queue.empty():
            node, level = queue.pop()
            if node == self.nil:
                continue
            levels.setdefault(level, [])
            levels[level].append(node)
            queue.push((node.left, level + 1))
            queue.push((node.right, level + 1))

        levels = sorted(levels.items(), key=lambda e: e[0])
        levels = [level for var, level in levels]
        return levels

    def print_level_nodes(self):
        for level in self.get_level_nodes():
            print(level)

    def level_key_list(self):
        data = []
        self.root.levelorder_walk(
            callback=lambda e: data.append(e.key),
            nil=self.nil
        )
        return data

    def inorder_walk(self, callback=print):
        self.root.inorder_walk(callback, self.nil)

    def preorder_walk(self, callback=print):
        self.root.preorder_walk(callback, self.nil)

    def postorder_walk(self, callback=print):
        self.root.postorder_walk(callback, self.nil)

    def levelorder_walk(self, callback=print):
        self.root.levelorder_walk(callback, self.nil)

    def _update_height(self, node):
        node.parent_walk(
            callback=lambda e: e._update_height(),
            nil=self.nil
        )


class SearchNode(BinaryNode):

    pass


class SearchTree(BinaryTree):

    def __init__(self, keys=[], random=False):
        super().__init__()
        self.build(keys, random)

    def build(self, keys: list, random=False):
        if random:
            import random as r
            r.shuffle(keys)
        for key in keys:
            self.insert(key)

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

    def predecessor(self, node):
        if node.left != self.nil:
            return self.maximum(node.left)
        parent = node.parent
        while parent != self.nil and node == parent.left:
            node = parent
            parent = node.parent

        if parent == self.nil:
            return None
        return parent

    def insert(self, key, data=None):
        node = self._init_node(key=key, data=data)
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

        self._size += 1

        self._update_height(node)

        return node

    def _transplant(self, node, replace):
        if replace != self.nil:
            replace.parent = node.parent

        parent = node.parent
        if parent == self.nil:
            self.root = replace
        elif node.is_left():
            parent.left = replace
        else:
            parent.right = replace
        self._update_height(replace)
        self._update_height(parent)

    def delete(self, key):
        node = self.search(key)
        if not node:
            return None

        middle = node

        if (node.left, node.right) == (self.nil, self.nil):
            replace = node.parent
            self._transplant(node, self.nil)

        elif node.left == self.nil:
            replace = node.right
            self._transplant(node, replace)

        elif node.right == self.nil:
            replace = node.left
            self._transplant(node, replace)

        else:
            middle = self.minimum(node.right)
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

        node.free()
        self._size -= 1
        return replace
