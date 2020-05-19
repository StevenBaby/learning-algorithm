# coding=utf-8

from ..table.lists import LinkedNode, LinkedList


class LinkedGraphNode(LinkedNode):
    pass


class LinkedGraphList(LinkedList):

    Node = LinkedGraphNode
    pass


class LinkedGraph(object):
    pass
