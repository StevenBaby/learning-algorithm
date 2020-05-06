# coding=utf-8

from node import Node


class ListNode(Node):

    def __init__(self, value=None):
        super().__init__(value)
        self.next = None


class List(object):

    def __init__(self):
        self.head = ListNode()
        self.tail = self.head

    def append(self, node):
        if not isinstance(node, ListNode):
            node = ListNode(node)
        self.tail.next = node
        self.tail = node

    def print(self):
        if self.head == self.tail:
            return
        node = self.head.next
        while node:
            print(node)
            node = node.next


if __name__ == '__main__':
    list = List()
    list.append(1)
    list.append(7)
    list.append(9)
    list.append(6)
    list.print()
