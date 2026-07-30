# 8th july 2026
# our company network has n computers some are directly connected find how many isolated network exist.
class Graph:
    graph=[]
    def countNetworks(self):
    visited = [False] * len(self.graph)
    count = 0

    for i in range(1, len(self.graph)):
        if not visited[i]:
            self.dfs(i, visited)   
            count += 1
            print()

    return count

g1 = Graph()
g1.creategraph(6)

g1.addedge(1,2)
g1.addedge(2,3)
g1.addedge(4,5)