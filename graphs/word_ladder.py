from Graph import Graph
from Graph import Queue

def buildGraph(wordFile):
    d = {}
    g = Graph()

    with open(wordFile, 'r') as wfile:
        for line in wfile:
            for w in line.split():
                for i in range(len(w)):
                    bucket = w[:i] + '_' + w[i+1:]
                    print(bucket)
                    if bucket in d:
                        d[bucket].append(w)
                    else:
                        d[bucket] = [w]
        for bucket in d.keys():
            for word1 in d[bucket]:
                for word2 in d[bucket]:
                    if word1 != word2:
                        g.addEdge(word1, word2)
    return g


def bfs(g, start):
    start.setDistance(0)
    start.setPred(None)
    vertQueue = Queue()
    verQueue.enqueue(start)
    while vertQueue.size > 0:
        currentVert = vertQueue.dequeue()
        for nbr in currentVert.getConnections():
            if nbr.getColor == 'white':
                nbr.setColor('gray')
                nbr.setDistance(currentVert.getDistance()+1)
                nbr.setPred(currentVert)
                vertQueue.enqueue(nbr)
        currentVert.setColor('black')
        

buildGraph('words.txt')
