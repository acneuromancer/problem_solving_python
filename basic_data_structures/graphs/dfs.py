'''
DFS algorithm

Traversal means visiting all the nodes of a graph. Depth first traversal or Depth first Search is a recursive algorithm for searching all the vertices of a graph or tree data structure. In this article, you will learn with the help of examples the DFS algorithm, DFS pseudocode and the code of the depth first search algorithm with implementation in C++, C, Java and Python programs.
DFS algorithm

A standard DFS implementation puts each vertex of the graph into one of two categories:

    Visited
    Not Visited

The purpose of the algorithm is to mark each vertex as visited while avoiding cycles.

The DFS algorithm works as follows:

    Start by putting any one of the graph's vertices on top of a stack.
    Take the top item of the stack and add it to the visited list.
    Create a list of that vertex's adjacent nodes. Add the ones which aren't in the visited list to the top of stack.
    Keep repeating steps 2 and 3 until the stack is empty.
'''


def dfs(graph, start, visited = None):
    if visited is None:
        visited = set()

    visited.add(start)
    print(start)

    for next in graph[start] - visited:
        dfs(graph, next, visited)

    return visited


graph = {'0': set(['1', '2']),
    '1': set(['0', '3', '4']),
    '2': set(['0']),
    '3': set(['1']),
    '4': set(['2', '3'])
}

dfs(graph, '0')
