#!/usr/bin/python
# Copyright (C) 2012 Dennis Francis<dennisfrancis.in@gmail.com>

import random

class ErdosRenyiModel(object):
    def __init__(self, n, edge_probability, graphds):
        self.n = n
        self.edge_probability = edge_probability
        self.graphds = graphds
        
    def generate(self):
        for i in xrange(2,n+1):
            for j in xrange(1,i):
                if random.random() >= self.edge_probability:
                    self.graphds.add_edge(i, j, 1)
        
    
