class Vertex(object):
    def __init__(self, key):
        self.key = key
        self.neighbours = {}

    def add_neighbour(self, neighbour, weight = 0):
        self.neighbours[neighbour] = weight

    def __str__(self):
        return '{} neighbours: {}'.format(
            self.key,
            [x.key for x in self.neighbours]
        )

    def get_connections(self):
        return self.neighbours.keys()

    def get_weight(self, neighbour):
        return self.neighbours[neighbour]


class Graph(object):
    def __init__(self):
        self.verticies = {}

    def add_vertex(self, vertex):
        self.verticies[vertex.key] = vertex

    def get_vertex(self, key):
        try:
            return self.verticies[key]
        except KeyError:
            return None
    
    def __contains__(self, key):
        return key in self.verticies

    def add_edge(self, from_key, to_key, weight = 0):
        if from_key not in self.verticies:
            self.add_vertex(Vertex(from_key))
        if to_key not in self.verticies:
            self.add_vertex(Vertex(to_key))
        self.verticies[from_key].add_neighbour(self.verticies[to_key], weight)

    def get_verticies(self):
        return self.verticies.keys()
        
    def __iter__(self):
        return iter(self.verticies.values())


g = Graph()
for i in range(6):
    g.add_vertex(Vertex(i))
print(g.verticies)
g.add_edge(0, 1, 5)
g.add_edge(0, 5, 2)
g.add_edge(1, 2, 4)
g.add_edge(2, 3, 9)
g.add_edge(3, 4, 7)
g.add_edge(3, 5, 3)
g.add_edge(4, 0, 1)
g.add_edge(5, 4, 8)
g.add_edge(5, 2, 1)

for v in g:
    for w in v.get_connections():
        print('{} -> {}'.format(v.key, w.key))