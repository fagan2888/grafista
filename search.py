#!/usr/bin/python


from collections import deque
from utils import Heap

class Search(object):
    def __init__(self, graph):
        self.graph = graph
        
    def bfs(self, start_node):
        open_list = deque([start_node])
        pathprev = { start_node:None }
        dist = { start_node:0 }
        while open_list:
            n = open_list.popleft()
            for adj in self.graph.get_neighbours(n):
                if adj not in dist:
                    open_list.append(adj)
                    dist[adj] = dist[n] + 1
                    pathprev[adj] = n
        return dist, pathprev

    def dijkstra(self, s):
        sdist = dict( ((n, 1E9) for n in self.graph.nodes()) )
        sdist[s] = 0
        pathprev = { s:None }
        marked = {}
        pq = [ [sdist[n], n] for n in self.graph.nodes() ]
        Ref = dict([ (pq[i][1],i) for i in range(len(pq)) ])
        heap = Heap(pq, Ref)
        heap.heapify()
        #print pq
        #print Ref
        while pq:
            node_distance, node = heap.heappop()
            marked[node] = True
            for nei in self.graph.get_neighbours(node):
                if nei not in marked:
                    nei_new_dist = node_distance + self.graph.get_weight(nei, node)
                    if sdist[nei] > nei_new_dist:
                        #print pq
                        heap.decrease_key(Ref[nei], nei_new_dist)
                        #print pq
                        sdist[nei] = nei_new_dist
                        pathprev[nei] = node
        return sdist, pathprev
        
        
def test():
    from ds import Graph
    g = Graph()
    edges = [['a','b', 1], ['a','c',1], ['b','d',1], ['c','d', 1], ['b', 'e', 1],
             ['c','f',1], ['e','h',1], ['f', 'h', 1], ['d', 'h', 1], ['h', 'g', 1],
             ['c', 'g', 1], ['b', 'h', 1]]
    g.add_edges(edges)
    s = Search(g)
    dist, pathprev = s.bfs('a')
    assert dist['g'] == 2
    assert dist['h'] == 2
    assert dist['d'] == 2
    assert dist['b'] == 1
    assert pathprev['g'] == 'c'
    assert pathprev['h'] == 'b'
    edges = [ (1,2,1), (1,3,7), (2,3,2), (2,4,3), (3,4,4), (3,5,5), (4,5,1), (4,7,3), 
              (4,6,5), (5,6,1), (5,8,2),(7,9,1), (7,10,5), (6,10,1), (8,11,6), (8,12,1) ]
    g = Graph()
    g.add_edges(edges)
    s = Search(g)
    dist, pathprev = s.dijkstra(1)
    assert dist[5] == 5
    assert dist[7] == 7
    assert dist[9] == 8
    assert dist[11] == 13
    assert dist[12] == 8
    assert pathprev[4] == 2
    assert pathprev[7] == 4
    assert pathprev[11] == 8
    assert pathprev[8] == 5
    assert pathprev[12] == 8
    
    
    
if __name__ == '__main__':
    test()
    
