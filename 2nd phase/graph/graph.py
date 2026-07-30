# 08 july 2026
# graph implementation
class Graph:
    graph=[]
    def creategraph(self,v):
        for i in range(1,v+2):
            self.graph.append([])

    def addedge(self,src,dest):
        self.graph[src].append(dest)
        self.graph[dest].append(src)

    def removeEdge(self,src,dest):
        self.graph[src].remove(dest)
        self.graph[dest].remove(src)

    def dfs(self,src,visited):
        visited[src]=True
        print(src,end=" ")
        for neighbour in self.graph[src]:
            if(visited[neighbour]!= True):
                self.dfs(neighbour,visited)

    def bfs(self,src):
        visited=[]
        que=[]
        for i in range(len(self.graph)):
            visited.append(False)
        que.append(src)
        visited[src]
        while len(que)!=0:
            curr=que[0]
            del que[0]
            print(curr,end=" ")
            for neighbour in self.graph[curr]:
                if visited[neighbour]!=True:
                    que.append(neighbour)
                    visited[neighbour]=True  

    def hascycle(self,src,visited,parent):
        visited[src]=True

        for neighbour in self.graph[src]:
            if visited[neighbour]!=True:
                if self.hascycle(neighbour,visited,src):
                    return True
                elif neighbour!= parent:
                    return True
                
            return False    
        
    # number of island 
    def countcomponent(self):
        visited = [False] * len(self.graph)
        count=0

        for i in range(1, len(self.graph)):
            if visited[i]!= True:
                self.dfs(i, visited)
                count += 1

        return count
    
    def countNetworks(self):
        visited = [False] * len(self.graph)
        count = 0

        for i in range(1, len(self.graph)):
            if not visited[i]:
                self.dfs(i, visited)   
                count += 1
                print()

        return count

g1=Graph()
# g1.creategraph(6)
# g1.addedge(1,2)
# g1.addedge(2,3)
# g1.addedge(2,5)
# g1.addedge(3,4)
# g1.addedge(4,5)
# g1.addedge(4,1)
# g1.addedge(5,6)

g1.creategraph(7)
g1.addedge(1,2)
g1.addedge(3,4)
g1.addedge(4,5)
g1.addedge(3,5)
g1.addedge(5,6)

# g1.dfs(1,[False,False,False,False,False,False,False])
# g1.bfs(1)
print("No. of Islands =", g1.countcomponent())
#   our company network has 