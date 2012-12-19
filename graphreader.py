#!/usr/bin/python
# Copyright (C) 2012 Dennis Francis<dennisfrancis.in@gmail.com>

class GraphReader(object):

    def __init__(self, fname, graphds, skip_first_line=False):
        self.fname = fname
        self.graphds = graphds
        self.skip_first_line = skip_first_line
        
    def read(self):
        f = file(self.fname, "r")
        if self.skip_first_line:
            f.readline()
        for line in f:
            n1, n2, wt = line.strip().split(" ")
            wt = int(wt)
            self.graphds.add_edge(n1, n2, wt)
            
