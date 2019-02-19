from Graph import Graph
from Graph import Queue

def buildGraph(wordFile):
    d = {}
    g = Graph()

    with open(wordFile, 'r') as wfile:
        d = {}
        g = Graph()

        for line in wfile:
            word = line[:-1]

            for i in range(len(word)):
                bucket = word[:i] + '_' + word[i+1:]
                if bucket in d:
                    d[bucket].append(word)
                else:
                    d[bucket]  = [word]

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
    vertQueue.enqueue(start)
    while vertQueue.size() > 0:
        currentVert = vertQueue.dequeue()
        for nbr in currentVert.getConnections():
            if nbr.getColor == 'white':
                nbr.setColor('gray')
                nbr.setDistance(currentVert.getDistance()+1)
                nbr.setPred(currentVert)
                vertQueue.enqueue(nbr)
        currentVert.setColor('black')


def traverse(y):
    x = y
    while (x.getPred()):
        print(x.getPred())
        x = x.getPred()
    print(x.getId())


g = buildGraph("words_shorter.txt")
for i in g.keysprint(g)

# bfs(g, g.getVertex('fool'))
# traverse(g.getVertex('sage'))
