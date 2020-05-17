# coding=utf-8

from .direct import BaseTable
from .lists import DoubleLinkedNode, DoubleLinkedList


class ChainHashNode(DoubleLinkedNode):

    def __init__(self, data=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.data = data


class ChainHashList(DoubleLinkedList):

    Node = ChainHashNode

    def insert(self, key, data=None):
        node = super().insert(0, key)
        node.data = data
        return node


class ChainHashTable(BaseTable):

    def __init__(self):
        self._size = 0
        self.slots = [ChainHashList() for _ in range(4)]

    def _factor(self):
        return self.size() / len(self.slots)

    def _hash(self, key):
        return key % len(self.slots)

    def search(self, key):
        hashkey = self._hash(key)
        node = self.slots[hashkey].search(key)
        return node

    def insert(self, key, data=None):
        hashkey = self._hash(key)
        node = self.slots[hashkey].insert(key, data)
        self._size += 1
        return node

    def delete(self, key):
        hashkey = self._hash(key)
        node = self.slots[hashkey].delete(key)
        self._size -= 1
        return node
