import sys

class Queue:

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


class Vertex:

    def __init__(self, key):
        self.id = key
        self.connectedTo = {}
        self.colort = 'white'
        self.dist = sys.maxsize
        self.pred = None
        self.disc = 0
        self.fin = 0

    def addNeighbour(self, nbr, weight = 0):
        self.connectedTo[nbr] = weight

    def setColor(self, color):
        self.color = color

    def setDistance(self, d):
        self.dist = d

    def setPred(self, p):
        self.pred = p

    def setDiscovery(self, dtime):
        self.disc = dtime

    def setFinish(self, ftime):
        self.fin = ftime

    def getFinish(self):
        return self.fin

    def getPred(self):
        return self.pred

    def getDistance(self):
        return self.dist

    def getColor(self):
        return self.color

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self, nbr):
        return self.connectedTo[nbr]

    def __str__(self):
        return str(self.id) + ' connected to ' + str([x.id for x in self.connectedTo])


class Graph:

    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self, key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self, n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self, n):
        return n in self.vertList

    def addEdge(self, f, t, cost = 0):
        if f not in self.vertList:
            nv = self.addVertex(f)

        if t not in self.vertList:
            nv = self.addVertex(t)

        self.vertList[f].addNeighbour(self.vertList[t], cost)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())
