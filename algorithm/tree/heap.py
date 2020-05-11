# coding=utf-8

from .binary import BinaryTree


class Heap(BinaryTree):

    MAX = 1
    MIN = 2

    def __init__(self, type=MAX):
        super().__init__()
        self.type = type
        self._size = None

    def size(self):
        if self._size is not None:
            return self._size
        return len(self)

    def compare(self, parent, child):
        if self.type == Heap.MAX:
            return self[parent] > self[child]
        elif self.type == Heap.MIN:
            return self[parent] < self[child]

    def heapify(self, index):
        left = self.left(index)
        right = self.right(index)

        if left < self.size() and not self.compare(index, left):
            exchange = left
        else:
            exchange = index
        if right < self.size() and not self.compare(exchange, right):
            exchange = right

        if exchange != index:
            # exchange index
            temp = self[index]
            self[index] = self[exchange]
            self[exchange] = temp
            self.heapify(exchange)

    def build(self):
        for index in range(self.size() // 2, -1, -1):
            self.heapify(index)

    def sort(self):
        for index in range(self.size() - 1, 0, -1):
            temp = self[0]
            self[0] = self[index]
            self[index] = temp
            self._size = self.size() - 1
            self.heapify(0)


class PriorityQueue(Heap):

    def top(self):
        return self[0]

    def insert(self, key):
        self.append(-float('inf'))
        self.increase_key(self.size() - 1, key)

    def extract(self):
        if self.size() < 1:
            return None
        top = self[0]
        self[0] = self[self.size() - 1]
        self.pop()
        self.heapify(0)
        return top

    def increase_key(self, index, key):
        if key < self[index]:
            raise Exception('New key is smaller than current key')
        self[index] = key
        while index > 0 and not self.compare(self.parent(index), index):
            temp = self[index]
            self[index] = self[self.parent(index)]
            self[self.parent(index)] = temp
            index = self.parent(index)
