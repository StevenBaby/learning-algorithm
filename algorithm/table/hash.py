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
        self._slot_size_before = 3
        self._slot_size = 5
        self._slots = [ChainHashList() for _ in range(self._slot_size)]

        # other
        # self._multiple_factor = 0.618033988  # by Knuth
        import random  # TODO remove random implementation by self
        self._multiple_factor = random.random()

        self.realm_prime = 113423713055421844361000443  # any large prime
        self.realm_a = int((random.random() * self.realm_prime) - 1)
        self.realm_b = int((random.random() * self.realm_prime))

    def _factor(self):
        return self._size / self._slot_size

    def _hash_mod(self, key):
        return key % self._slot_size

    def _hash_multiply(self, key):

        return int(self._slot_size * ((self._multiple_factor * key) % 1))

    def _hash_realm(self, key):
        hashkey = (
            (self.realm_a * key + self.realm_b) % self.realm_prime
        ) % self._slot_size
        return hashkey

    def _hash(self, key):
        # return self._hash_mod(key)
        # return self._hash_multiply(key)
        return self._hash_realm(key)

    def search(self, key):
        hashkey = self._hash(key)
        node = self._slots[hashkey].search(key)
        return node

    def insert(self, key, data=None):
        hashkey = self._hash(key)
        node = self._slots[hashkey].insert(key, data)
        self._size += 1
        return node

    def delete(self, key):
        hashkey = self._hash(key)
        node = self._slots[hashkey].delete(key)
        self._size -= 1
        return node
