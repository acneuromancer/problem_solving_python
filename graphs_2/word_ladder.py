from collections import defaultdict
from collections import deque
from itertools import product
# import os

def build_graph(words):
    buckets = defaultdict(list)
    graph = defaultdict(set)

    for word in words:
        for i in range(len(word)):
            bucket = '{}_{}'.format(word[:i], word[i+1:])
            buckets[bucket].append(word)

    for bucket, mutual_neighbours in buckets.items():
        for word1, word2 in product(mutual_neighbours, repeat = 2):
            if word1 != word2:
                graph[word1].add(word2)
                graph[word2].add(word1)

    return graph

def get_words(vocabulary_file):
    with open(vocabulary_file, 'r') as words_file:
        for line in words_file:
            yield line[:-1]


def traverse(graph, starting_vertex):
    visited = set()
    queue = deque([[starting_vertex]])
    while(queue):
        path = queue.popleft()
        vertex = path[-1]
        yield vertex, path
        for neighbour in graph[vertex] - visited:
            visited.add(neighbour)
            queue.append(path + [neighbour])


word_graph = build_graph(get_words('words_shorter.txt'))
for k, v in word_graph.items():
    print('{} -> {}'.format(k, v))

for vertex, path in traverse(word_graph, 'fool'):
    if vertex == 'sage':
        print(' -> '.join(path))