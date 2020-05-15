# coding=utf-8


class AVLNode(BinaryNode):
    pass
    # def __str__(self):
    #     return super().__str__()

    # def __repr__(self):
    #     return super().__repr__()


class AVLTree(BinaryTree):

    def __init__(self):
        self.nil = AVLNode()
        self.root = self.nil
