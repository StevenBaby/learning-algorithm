# coding=utf-8


class LinkedNode(object):
    pass


class LinkedList(object):

    def __init__(self):
        pass

    def next(self):
        pass

    def search(self, key):
        pass

    def insert(self, key):
        pass

    def delete(self, key):
        pass


class DoubleLinkedNode(LinkedNode):
    pass


class DoubleLinkedList(LinkedList):

    def __init__(self):
        self.head = None

    def prev(self):
        pass


class NilDoubleLinkedList(DoubleLinkedList):

    def __init__(self):
        super().__init__()
        self.nil = DoubleLinkedNode()


class CircularList(DoubleLinkedList):
    pass
