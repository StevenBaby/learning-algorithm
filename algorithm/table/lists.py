# coding=utf-8


class LinkedNode(object):

    def __init__(self, key=None, next=None):
        self.key = key
        self.next = next

    def __str__(self):
        if self.key is None:
            return 'nil'
        return f'{self.key}'

    def __repr__(self):
        return self.__str__()


class LinkedList(object):

    Node = LinkedNode

    def __init__(self, keys=[]):
        self.nil = self.Node()
        self.head = self.nil
        self._size = 0

        for key in keys:
            self.append(key)

    def _init_node(self, key):
        node = self.Node(key=key, next=self.nil)
        return node

    def append(self, key):
        pass


class DoubleLinkedNode(LinkedNode):

    def __init__(self, prev=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.prev = prev


class DoubleLinkedList(object):

    Node = DoubleLinkedNode

    def __init__(self, keys=[]):
        self.nil = self.Node()
        self.head = self.nil
        self.tail = self.nil
        self._size = 0

        for key in keys:
            self.append(key)

    def _init_node(self, key):
        node = self.Node(key=key, next=self.nil, prev=self.tail)
        return node

    def search(self, key):
        node = self.head
        while node != self.nil:
            if node.key == key:
                return node
            node = node.next

    def append(self, key):
        node = self._init_node(key)
        if self.tail == self.nil:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node

        self.tail = node
        self._size += 1
        return node

    def pop(self):
        if self.tail == self.nil:
            return None
        node = self.tail
        self.tail = self.tail.prev
        self._size -= 1
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

    def insert(self, index, key):
        place = self.get(index)
        if not place:
            return self.append(key)

        node = self._init_node(key=key)
        node.next = place
        node.prev = place.prev
        place.prev.next = node
        place.prev = node

        if node.prev == self.nil:
            self.head = node
        self._size += 1

    def delete(self, key):
        node = self.search(key)
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

        self._size -= 1

    def walk(self, callback=print, stop=None):
        node = self.head
        for index in range(self.size()):
            callback(node)
            if stop is not None and stop(index, node):
                break
            node = node.next

    def print_list(self):
        nodes = []
        self.walk(callback=lambda e: nodes.append(e))
        print(nodes)

    def size(self):
        return self._size

    def empty(self):
        return self._size == 0


class CircularList(DoubleLinkedList):

    def __init__(self, keys=[]):
        self.nil = self.Node()
        self.head = self.nil
        self._size = 0

        for key in keys:
            self.append(key)

    def _init_node(self, key):
        node = self.Node(key=key)
        return node

    def search(self, key):
        if self.head.key == key:
            return self.head

        node = self.head.next
        while node != self.head:
            if node.key == key:
                return node
            node = node.next

    def append(self, key):
        node = self._init_node(key=key)
        if self.head == self.nil:
            self.head = node
            node.next = node
            node.prev = node
        else:
            tail = self.head.prev
            self.head.prev = node
            node.prev = tail
            tail.next = node
            node.next = self.head

        self._size += 1

    def pop(self):
        if self.empty():
            return None
        if self.size() == 1:
            node = self.head
            self.head = self.nil
        else:
            node = self.head.prev
            tail = node.prev
            tail.next = self.head
            self.head.prev = tail

        self._size -= 1
        return node

    def get(self, index):
        if self.empty():
            return None

        node = self.head
        index %= self.size()

        for _ in range(index):
            node = node.next
        return node

    def insert(self, index, key):
        place = self.get(index)
        if not place:
            return self.append(key)

        node = self._init_node(key=key)
        node.next = place
        node.prev = place.prev
        place.prev.next = node
        place.prev = node

        self._size += 1

    def delete(self, key):
        node = self.search(key)
        if not node:
            return
        if self.size() == 1:
            self.head = self.nil
        else:
            prev = node.prev
            next = node.next
            prev.next = next
            next.prev = prev
            if node == self.head:
                self.head = next

        self._size -= 1
