# coding=utf-8

from .direct import BaseTable


class HashNode(object):

    def __init__(self, key, data):
        self.key = key
        self.data = data


class ChainHashTable(BaseTable):

    Node = HashNode

    def _init_node(self, key, data):
        node = self.Node(key=key, data=data)
        return node
