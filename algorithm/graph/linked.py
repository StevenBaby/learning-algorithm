# coding=utf-8


WHITE = 0
GRAY = 1
BLACK = 2


class LinkedNode(object):

    def __init__(self, key=None, data=None):
        self.key = key
        self.data = data
        self.adj = []
        self._color = None
        self._distance = 0
        self._predecessor = None


class LinkedEdge(object):

    def __init__(self, weight=None):
        self._weight = weight

    def weight(self):
        return self._weight


class LinkedGraph(object):

    Node = LinkedNode
    Edge = LinkedEdge

    def __init__(self):
        self._vertex_size = 0
        self._edge_size = 0
        self.nodes = []
        self.edges = []

    def vertex_size(self):
        return self._vertex_size

    def edge_size(self):
        return self._edge_size

    def add_node(self, node):
        pass

    def print_path(self, before, after):
        import sys
        if before == after:
            sys.stdout.write(str(before))
            return
        if after._predecessor is None:
            print(f"no path from {before} to {after}")
            return
        self.print_path(self, before, after._predecessor)
        sys.stdout.write(f" > {after}")

    def _prepare_search(self):
        for node in self.nodes:
            node._color = WHITE
            node._distance = float('inf')
            node._predecessor = None

    def breadth_first_search(self, node, callback=print, stop=None):
        from algorithm.table.queue import Queue

        self._prepare_search()

        queue = Queue()
        node._color = GRAY
        node._distance = 0
        node._predecessor = None
        queue.clear()
        queue.push(node)

        while not queue.empty():
            parent = queue.pop()
            if callable(callback):
                callback(parent)
            if callable(stop) and stop(parent):
                return
            for child in parent.adj:
                if v.color != WHITE:
                    continue
                child.color = GRAY
                child._distance = parent._distance + 1
                child._predecessor = parent
                queue.push(child)
            parent.color = BLACK

    def _depth_visit(self, node, callback=print, stop=None):
        node._color = GRAY
        for child in node.adj:
            if child._color != WHITE:
                continue
            child._predecessor = node
            self._depth_visit(child, callback=callback, stop=stop)
        node._color = BLACK
        self.time += 1
        node._distance = self.time
        if callable(node):
            callback(node)
        if callable(stop) and stop(node):
            return

    def depth_first_search(self, callback=print, stop=None):
        self._prepare_search()

        self.time = 0
        for node in self.nodes:
            if node._color != WHITE:
                continue
            self._depth_visit(node, callback=callback, stop=stop)

    def topological_sort(self):
        from algorithm.table.lists import LinkedList
        list = LinkedList()
        self.depth_first_search(
            callback=lambda e: list.insert(0, e)
        )
        return list

    def strongly_connected_components(self):
        # TODO ......
        self.depth_first_search(callback=lambda e: (
            # compute GT
        ))
        self.depth_first_search(callback=lambda e: (
            # do something
        ))

    def generic_mst(self):
        # TODO...
        pass

    def get_weight(self, before, after):
        # TODO ...
        return 0

    def _init_single_source(self, node):
        for var self.nodes:
            var._distance = float('inf')
            var._predecessor = None
        node._distance = 0

    def _relax(self, before, after):
        distance = before._distance + self.get_weight(before, after)
        if after._distance > distance:
            after._distance = distance
            after._predecessor = before

    def _bellman_ford(self, node):
        self._init_single_source(node)
        for i in range(1, len(self.nodes)):
            for edge in self.edges:
                self._relax(edge.before, edge.after)
        for edge in self.edges:
            if edge.after > edge.before + edge.weight():
                return False
        return True

    def dag_shortest_paths(self, node):
        topology = self.topological_sort()
        self._init_single_source(node)
        for before in topology:
            for after in vertex.adj:
                self._relax(before, after)

    def dijkstra(self, node):
        self._init_single_source(node)
        from algorithm.tree.heap import PriorityQueue

        queue = PriorityQueue(type=PriorityQueue.MIN)
        queue.append(node)

        results = set()

        while not queue.empty():
            parent = queue.extract()
            results.add(parent)
            for child in parent.adj:
                self._relax(parent, child)
                if child not in results:
                    queue.append(child)
