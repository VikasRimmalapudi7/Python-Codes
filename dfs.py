from collections import defaultdict

class Graph:
    def __init__(self) :
        self.graph=defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)

    def dfs_traversal(self,visited,node):
        if node not in visited:
            visited.add(node)
            print(node,end='  ')
            for i in self.graph[node]:
                self.dfs_traversal(visited,i)

g=Graph()
g.addEdge(0,1)
g.addEdge(0,3)
g.addEdge(1,3)
g.addEdge(1,2)
g.addEdge(1,5)
g.addEdge(3,4)
g.addEdge(3,2)
g.addEdge(2,3)
g.addEdge(2,1)
g.addEdge(2,5)
g.addEdge(4,6)
g.addEdge(4,3)
g.addEdge(4,2)
g.addEdge(6,4)
g.addEdge(6,2)
g.dfs_traversal(set(),0)

