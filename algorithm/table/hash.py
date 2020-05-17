# coding=utf-8


class HashNode(object):

    def __init__(self, key, data):
        self.key = key
        self.data = data


class BaseHashTable(object):

    Node = HashNode

    def __init__(self):
        self._size = 0

    def _init_node(self, key, data):
        node = self.Node(key=key, data=data)
        return node

    def size(self):
        return self._size

    def search(self, key):
        pass

    def insert(self, key, data):
        pass

    def delete(self, key):
        pass


class DirectAddressTable(BaseHashTable):

    def __init__(self, size: int):
        self._size = size
        self.slots = [None for _ in range(size)]

    def is_valid_key(self, key):
        return 0 <= key < self.size()

    def search(self, key):
        if not self.is_valid_key(key):
            return None
        return self.slots[key]

    def insert(self, key, data):
        if not self.is_valid_key(key):
            return None
        self.slots[key] = data

    def delete(self, key):
        if not self.is_valid_key(key):
            return None
        self.slots[key] = None
