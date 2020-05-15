# coding=utf-8

from .binary import SearchNode, SearchTree


class AVLNode(SearchNode):
    pass


class AVLTree(SearchTree):

    Node = AVLNode
