from collections import defaultdict
from itertools import product
import os

from Graph import Graph
from Graph import Queue

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


g = build_graph(get_words('words_shorter.txt'))

for key, val in g.items():
    print(key, val)
