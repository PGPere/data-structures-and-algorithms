from collections import defaultdict
from csv import list_dialects


class Graph:

    def __init__(self):
        self.graph = defaultdict(list)
        self.vertex = {}

    def add_node(self, node):
        newVertex = Vertex(node)
        self.vertex[node] = newVertex
        return newVertex

    def add_edge(self, from_v, to_v, weight=0):
        if from_v not in self.vertex:
            self.add_node(from_v)
        if to_v not in self.vertex:
            self.add_node(to_v)
        self.vertex[from_v].addNeighbor(self.vertex[to_v], weight)

    def get_nodes(self):
        return self.vertex.keys()

    def get_neighbors(self, n):
        list_neighbors = []
        for w in self.vertex[n].getConnections():
            #     #     # print("({} -> {})".format(self.vertex[n].value, w.value))
            #     #     # list_neighbors.append("{}".format(w.value))
            #     #     # list_neighbors.append(
            #     #     #     "({} -> {})".format(self.vertex[n].value, w.value))
            #     #     list_neighbors.append(
            #     #         "({} -> {})".format(self.vertex[n].value, w.value))
            #     #     print(list_neighbors)
            #     #     return list_neighbors
            #     node = self.vertex[n]
            #     print(Vertex.getConnections(w))
            #     list_neighbors.append(Vertex.getConnections(w))
            # return "( %s)" % (w.getId())

            list_neighbors.append(w.getId().value)
            return list_neighbors

    def size(self):
        return len(self.get_nodes())

    def __iter__(self):
        return iter(self.vertex.values())

    def __contains__(self, value):
        return value in self.vertex


class Vertex:
    # def __init__(self, value):
    #     self.value = value
    #     self.next = None

    def __init__(self, value):
        self.value = value
        self.neighbors = {}

    def addNeighbor(self, neighbor, weight=0):
        self.neighbors[neighbor] = weight

    def __str__(self):
        # return '{} neighbors: {}'.format(self.value, [x.value for x in self.neighbors])
        # nbrs = [x.value for x in self.neighbors]
        # return '{}:{}'.format(self.value, nbrs)
        return str(self.value) + ' -->' + str([x.value for x in self.neighbors])

    def getConnections(self):
        return self.neighbors.keys()

    def getId(self):
        return self.value

    def getWeight(self, neighbor):
        return self.neighbors[neighbor]


class Edge:
    def __init__(self, vertex, weight=1):
        self.vertex = vertex
        self.weight = weight
