from collections import defaultdict

class Graph:
    def __init__(self) :
        self.graph=defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)

    def bfs_traversal(self,node):
        visited=[]
        queue=[]
        queue.append(node)
        visited.append(node)
        while queue:  
            node=queue.pop(0)
            print(node,end='  ')
            for i in self.graph[node]:
                if i not in  visited:
                    visited.append(i)
                    queue.append(i)

g=Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

g.bfs_traversal(2)

