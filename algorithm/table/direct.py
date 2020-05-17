# coding=utf-8


class BaseTable(object):

    def __init__(self):
        self._size = 0

    def size(self):
        return self._size

    def search(self, key):
        pass

    def insert(self, key, data):
        pass

    def delete(self, key):
        pass


class DirectAddressTable(BaseTable):

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
