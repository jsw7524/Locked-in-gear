import sys
import math

class Graph(object):
    def __init__(self, n):    
        self.graph={ i:[] for i in range(n)}
    def AddEdge(self, i, j):
        self.graph[i].append(j)
        self.graph[j].append(i)        
            
        
class BipartiteChecker(object):
    def __init__(self, n, graph):
        self.bipartite=[-1]*n
        self.graph=graph
        self.n=n
    def Check(self):
        self.DFS(0, 0 )
        for a in range(self.n):
            for b in self.graph.graph[a]:
                if -1==self.bipartite[a]:
                    break
                if (self.bipartite[a]+self.bipartite[b])%2==0:
                    return False
        return True
                
    
    def DFS(self, node, depth):
        self.bipartite[node]=depth
        for nextNode in self.graph.graph[node]:
            if -1==self.bipartite[nextNode]:
                self.DFS(nextNode, depth+1)
        
class Gear(object):
    def __init__(self, x, y, r):
        self.x=x
        self.y=y
        self.r=r
                    
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

#################

gears=[]
n = int(input())
for i in range(n):
    x, y, r = [int(j) for j in input().split()]
    gears.append(Gear(x, y, r))

graph=Graph(n)    
for a in range(n):
    for b in range(a+1,n):
        if (gears[b].x-gears[a].x)**2 +(gears[b].y-gears[a].y)**2 == (gears[b].r+gears[a].r)**2:
            graph.AddEdge(a,b)
    
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

bipartiteChecker=BipartiteChecker(n,graph)
workable=bipartiteChecker.Check()
if workable and -1==bipartiteChecker.bipartite[n-1]:
    print("NOT MOVING")
else:
    if 0==bipartiteChecker.bipartite[n-1]%2:
        print("CW")
    else:
        print("CCW")        
        
#################

#################