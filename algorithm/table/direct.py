# coding=utf-8


class BaseTable(object):

    def __init__(self):
        self._size = 0

    def size(self):
        return self._size

    def empty(self):
        return self._size == 0

    def search(self, key):
        pass

    def insert(self, key, data):
        pass

    def delete(self, key):
        pass


class DirectAddressTable(BaseTable):

    def __init__(self, size: int):
        self._bucket_size = size
        self._size = 0
        self._bucket = [None for _ in range(size)]

    def _factor(self):
        return self._size / self._bucket_size

    def is_valid_key(self, key):
        return 0 <= key < self._bucket_size

    def _hash(self, key):
        if not self.is_valid_key(key):
            return None
        return key

    def search(self, key):
        hashkey = self._hash(key)
        if hashkey is None:
            return None
        return self._bucket[hashkey]

    def insert(self, key, data):
        hashkey = self._hash(key)
        if hashkey is None:
            return None
        self._bucket[hashkey] = data
        self._size += 1

    def delete(self, key):
        hashkey = self._hash(key)
        if hashkey is None:
            return None
        self._bucket[hashkey] = None
        self._size -= 1


class OpenNode(object):

    def __init__(self, key=None, data=None):
        self.key = key
        self.data = data
        self.delete = False

    def __str__(self):
        if self.delete:
            return "DELETED"
        return f'{self.key} - {self.data}'

    def __repr__(self):
        return self.__str__()


class OpenAddressTable(DirectAddressTable):

    Node = OpenNode

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.quadratic_c_1 = 1
        self.quadratic_c_2 = 1

    def _hash_linear_probing(self, key, index):
        return (key + index) % self._bucket_size

    def _hash_key(self, key, index):
        return self._hash_linear_probing(key, index)

    def _hash_insert(self, key):
        index = 0
        hashkey = self._hash_key(key, index)
        node = self._bucket[hashkey]
        while node and not node.delete:
            index += 1
            hashkey = self._hash_key(key, index)
            node = self._bucket[hashkey]
        return hashkey

    def _hash_search(self, key):
        index = 0
        hashkey = self._hash_key(key, index)
        node = self._bucket[hashkey]
        start = node
        while node:
            if node.key == key and not node.delete:
                break

            index += 1
            hashkey = self._hash_key(key, index)
            node = self._bucket[hashkey]
            if node == start:
                return None

        if node and key == node.key and not node.delete:
            return hashkey
        return None

    def insert(self, key, data):
        if self._bucket_size == self._size:
            raise Exception('Table is full')
        hashkey = self._hash_insert(key)
        node = self.Node(key=key, data=data)
        super().insert(hashkey, node)

    def search(self, key):
        hashkey = self._hash_search(key)
        if hashkey is None:
            return
        node = super().search(hashkey)
        if not node:
            return None
        return node.data

    def delete(self, key):
        hashkey = self._hash_search(key)
        if hashkey is None:
            return
        node = self._bucket[hashkey]
        node.delete = True
        self._size -= 1
