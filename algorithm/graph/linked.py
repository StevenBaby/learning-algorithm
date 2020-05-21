# coding=utf-8


class Vertex(object):
    pass


class Edge(object):

    def __init__(self, weight=None):
        self.weight = weight


class LinkedGraph(object):

    Node = Vertex

    def __init__(self):
        self._vertex_size = 0
        self._edge_size = 0

    def vertex_size(self):
        return self._vertex_size

    def edge_size(self):
        return self._edge_size

    def add_vertex(self, vertex):
        pass
