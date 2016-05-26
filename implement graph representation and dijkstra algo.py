import sys
import heapq

class DirectedWeghtedGraph:
     def __init__(self,V,edges):
        self.nodes = {v:set() for v in range(V)}
        for e in edges: self.nodes[e[0]].add(e)

class DijkstraSP(object): 
    def __init__(self,graph,s):
        self.nodes=graph.nodes
        self.distTo=[None]*len(self.nodes)
        self.distTo[s]=0
        self.pq=[(0,s)]
    
    def findSP(self):
        while self.pq:
            _,v=heapq.heappop(self.pq)
            for e in self.nodes[v]: self.relax(e)
            #print v,self.distTo
    
    def relax(self,e):
        v,w,dist=e
        if not self.distTo[w]:
            self.distTo[w]=self.distTo[v]+dist
            heapq.heappush(self.pq,(self.distTo[w],w))
        elif self.distTo[w]>self.distTo[v]+dist:
            old_dist=self.distTo[w]
            self.distTo[w]=self.distTo[v]+dist
            self.decreaseKey(old_dist,w)
        # we don't need visited, as visited nodes have shorter distTo 
        # that won't require computation any more.
            
    def decreaseKey(self,old_dist,w): #this implementation is o(n), 
        # but in theory with heapDict, could be done in o(logn)
        self.pq.remove((old_dist,w))
        heapq.heappush(self.pq,(self.distTo[w],w))
        
edges=[(0,1,5),(0,4,9),(0,7,8), (1,7,4),(1,2,12),(1,3,15),(2,3,3),(2,6,11),
       (3,6,9),(4,5,4),(4,6,20),(4,7,5),(5,2,1), (5,6,13),(7,2,7),(7,5,6)]
graph=DirectedWeghtedGraph(8,edges)
print graph.nodes

a=DijkstraSP(graph,0)
a.findSP()
print a.distTo