# coding=utf-8

from .list import LinkedList


class Queue(LinkedList):

    def push(self, data):
        self.append(data)

    def pop(self):
        if self.head == self.nil:
            return None
        node = self.head

        self.head = self.head.next
        if self.tail == node:
            self.tail = self.nil

        if self.head != self.nil:
            self.head.prev = self.nil

        self._length -= 1
        return node.data
