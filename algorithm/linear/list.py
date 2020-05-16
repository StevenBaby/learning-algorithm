# coding=utf-8


class LinkedNode(object):

    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

    def __str__(self):
        if self.data is None:
            return 'nil'
        return f'{self.data}'

    def __repr__(self):
        return self.__str__()


class LinkedList(object):

    Node = LinkedNode

    def __init__(self, datas=[]):
        self.nil = self.Node()
        self.head = self.nil
        self.tail = self.nil
        self._length = 0

        for data in datas:
            self.append(data)

    def search(self, data):
        node = self.head
        while node != self.nil:
            if node.data == data:
                return node
            node = node.next

    def append(self, data):
        node = self.Node(data=data, next=self.nil, prev=self.tail)
        if self.tail == self.nil:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node

        self.tail = node
        self._length += 1
        return node

    def pop(self):
        if self.tail == self.nil:
            return None
        node = self.tail
        self.tail = self.tail.prev
        self._length -= 1
        return node

    def get(self, index):
        node = self.head
        for _ in range(index):
            if node == self.nil:
                return None
            node = node.next
        if node == self.nil:
            return None
        return node

    def insert(self, index, data):
        place = self.get(index)
        if not place:
            return self.append(data)

        node = self.Node(data=data, next=place, prev=place.prev)
        place.prev.next = node
        place.prev = node

        if node.prev == self.nil:
            self.head = node
        self._length += 1

    def delete(self, data):
        node = self.search(data)
        if not node:
            return

        prev = node.prev
        next = node.next
        if prev == self.nil:
            self.head = next
        else:
            prev.next = next
        if next != self.nil:
            next.prev = prev

        self._length -= 1

    def walk(self, callback=print):
        node = self.head
        while node != self.nil:
            callback(node)
            node = node.next

    def print_list(self):
        nodes = []
        self.walk(callback=lambda e: nodes.append(e))
        print(nodes)

    def length(self):
        return self._length

    def empty(self):
        return self.head == self.nil


class CircularList(LinkedList):
    pass
