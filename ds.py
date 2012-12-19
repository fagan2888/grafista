#!/usr/bin/python
# Copyright (C) 2012 Dennis Francis<dennisfrancis.in@gmail.com>

"""
    Graph data structure using hash tables.(inspired by CS215@Udacity)
"""

NOEDGE = -99999

class Graph(object):
    def __init__(self, directed=False):
        self.directed = directed
        self.G = {}
        
    def add_node(self, node):
        self.G[node] = {}
        
    def del_node(self, node):
        if node in self.G:
            d = self.G.pop(node)
            if not self.directed:
                for n in d:
                    self.G[n].pop(node)
            else:
                for n in self.G:
                    if node in self.G[n]:
                        self.G[n].pop(node)
            return True
        return False
      
    def add_edge(self, n1, n2, wt):
        if not n1 in self.G:
            self.add_node(n1)
        if not n2 in self.G:
            self.add_node(n2)
        self.G[n1][n2] = wt
        if not self.directed:
            self.G[n2][n1] = wt
        
    def add_edges(self, edges):
        for edge in edges:
            self.add_edge(*edge)
        
    def del_edge(self, n1, n2):
        if not (n1 in self.G and n2 in self.G):
            return False
        self.G[n1].pop(n2)
        if not self.directed:
            self.G[n2].pop(n1)
            
    def clear(self):
        self.G = {}
        
    def nodes(self):
        return self.G.keys()
        
    def get_edges(self):
        edges = []
        for n1 in self.G:
            for n2 in self.G[n1]:
                edges.append((n1, n2, self.G[n1][n2]))
        return edges
        
    def get_weight(self, n1, n2):
        if not (n1 in self.G and n2 in self.G):
            return NOEDGE
        return self.G[n1][n2] if n2 in self.G[n1] else NOEDGE
        
    def get_neighbours(self, n):
        return self.G[n].keys() if n in self.G else []
        
        
       
def test():
    g = Graph(directed=True)
    edges = [(1,2,1), (1,3,2), (2,3,4)]
    g.add_edges(edges)
    assert set(edges) == set(g.get_edges())
    edges.pop()
    g.del_edge(2,3)
    assert set(edges) == set(g.get_edges())
    assert -99999 == g.get_weight(2,3)
    g = Graph(directed=True)
    edges = [(1,2,1), (1,3,2), (2,3,4)]
    g.add_edges(edges)
    assert set([2,3]) == set(g.get_neighbours(1))
    
if __name__ == '__main__':
    test()
    
