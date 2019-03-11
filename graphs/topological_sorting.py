from general_dfs import DFSGraph

g = DFSGraph()
g.addEdge(5, 2) 
g.addEdge(5, 0) 
g.addEdge(4, 0) 
g.addEdge(4, 1) 
g.addEdge(2, 3) 
g.addEdge(3, 1)

g.dfs()

result_list = [(v.getId(), v.getFinish()) for v in g]
result_list.sort(key = lambda x:x[1], reverse = True)
print(result_list)

