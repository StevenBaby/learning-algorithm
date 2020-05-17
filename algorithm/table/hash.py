# coding=utf-8

from .direct import BaseTable
from .lists import DoubleLinkedNode, DoubleLinkedList


class ChainHashNode(DoubleLinkedNode):
    pass


class ChainHashTable(BaseTable):

    def __init__(self):
        self._size = 0
        self.slots = [DoubleLinkedList() for _ in range(4)]

    def _factor(self):
        return self.size() / len(self.slots)

    def _hash(self, key):
        return key % len(self.slots)

    def search(self, key):
        hashkey = self._hash(key)
        list = self.slots[hashkey].search(key)
        node = list

    def insert(self, key, data):
        pass

    def delete(self):
        pass
