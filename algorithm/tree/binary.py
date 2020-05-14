

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

    def __init__(self):
        self.parent = None
        self.left = None
        self.right = None


class BinaryTree(object):

    def __init__(self):
        self.root = None
