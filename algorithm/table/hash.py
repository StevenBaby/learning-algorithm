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

    def insert_node(self, node):
        node.prev = self.nil
        if self.tail == self.nil:
            node.next = self.nil
            self.tail = node
            self.head = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node

        self._size += 1


class ChainHashTable(BaseTable):

    def __init__(self):
        self._size = 0
        self._bucket_size_before = 3
        self._bucket_size = 5
        self._bucket = [ChainHashList() for _ in range(self._bucket_size)]
        self._update_factor()

    def _update_factor(self):
        # other
        # self._multiple_factor = 0.618033988  # by Knuth
        import random  # TODO remove random implementation by self
        self._multiple_factor = random.random()

        self._realm_prime = 113423713055421844361000443  # any large prime
        # self._realm_a = int((random.random() * self._realm_prime) - 1)
        # self._realm_b = int((random.random() * self._realm_prime))
        self._realm_a = int((0.618033988 * self._realm_prime) - 1)
        self._realm_b = int((0.618033988 * self._realm_prime))

    def _factor(self):
        return self._size / self._bucket_size

    def _hash_mod(self, key):
        return key % self._bucket_size

    def _hash_multiply(self, key):

        return int(self._bucket_size * ((self._multiple_factor * key) % 1))

    def _hash_realm(self, key):
        hashkey = (
            (self._realm_a * key + self._realm_b) % self._realm_prime
        ) % self._bucket_size
        return hashkey

    def _hash(self, key):
        # return self._hash_mod(key)
        # return self._hash_multiply(key)
        return self._hash_realm(key)

    def _rehash(self):
        bucket_size = self._bucket_size_before + self._bucket_size
        self._bucket_size_before = self._bucket_size
        self._bucket_size = bucket_size

        bucket = self._bucket
        self._size = 0

        self._bucket = [ChainHashList() for _ in range(self._bucket_size)]
        # self._update_factor()

        def insert_node(node):
            hashkey = self._hash(node.key)
            self._bucket[hashkey].insert_node(node)
            self._size += 1

        for tree in bucket:
            tree.walk(callback=insert_node)

    def search(self, key):
        hashkey = self._hash(key)
        slot = self._bucket[hashkey]
        node = slot.search(key)
        return node

    def insert(self, key, data=None):
        if self._factor() > 0.8:
            self._rehash()

        hashkey = self._hash(key)
        slot = self._bucket[hashkey]
        node = slot.insert(key, data)
        self._size += 1
        return node

    def delete(self, key):
        hashkey = self._hash(key)
        slot = self._bucket[hashkey]
        node = slot.delete(key)
        self._size -= 1
        return node
