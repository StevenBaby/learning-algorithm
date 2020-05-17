# coding=utf-8

from .lists import DoubleLinkedList


class Steak(DoubleLinkedList):

    def push(self, data):
        self.append(data)

    def pop(self):
        return super().pop().data

    def top(self):
        if self.tail == self.nil:
            return None
        return self.tail.data
