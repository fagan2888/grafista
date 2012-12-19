#!/usr/bin/python
# Utility classes for graph algorithms
# Copyright (C) 2012 Dennis Francis<dennisfrancis.in@gmail.com>

class Heap(object):
    def __init__(self, L, Ref):
        """L   - Array to be converted as heap
                  Array members must be of the form
                  [key, item, ...]
           Ref - Ref[item] gives the current position of item in L"""
        self.L = L
        self.Ref = Ref
        
    def _parent(self,i): 
        return (i-1)/2
    def _left_child(self, i): 
        return 2*i+1
    def _right_child(self, i): 
        return 2*i+2
    def _is_leaf(self, i): 
        return (self._left_child(i) >= len(self.L)) and (self._right_child(i) >= len(self.L))
    def _one_child(self,i): 
        return (self._left_child(i) < len(self.L)) and (self._right_child(i) >= len(self.L))
        
    def down_heapify(self, i):
        # If i is a leaf, heap property holds
        if self._is_leaf(i): 
            return
        # If i has one child...
        if self._one_child(i):
            # check heap property
            if self.L[i] > self.L[self._left_child(i)]:
                # If it fails, swap, fixing i and its child (a leaf)
                self.Ref[self.L[i][1]], self.Ref[self.L[self._left_child(i)][1]] = self._left_child(i), i
                (self.L[i], self.L[self._left_child(i)]) = (self.L[self._left_child(i)], self.L[i])
            return
        # If i has two children...
        # check heap property
        if min(self.L[self._left_child(i)], self.L[self._right_child(i)]) >= self.L[i]: 
            return
        # If it fails, see which child is the smaller
        # and swap i's value into that child
        # Afterwards, recurse into that child, which might violate
        if self.L[self._left_child(i)] < self.L[self._right_child(i)]:
            # Swap into left child
            self.Ref[self.L[i][1]], self.Ref[self.L[self._left_child(i)][1]] = self._left_child(i), i
            (self.L[i], self.L[self._left_child(i)]) = (self.L[self._left_child(i)], self.L[i])
            self.down_heapify(self._left_child(i))
            return
        else:
            self.Ref[self.L[i][1]], self.Ref[self.L[self._right_child(i)][1]] = self._right_child(i), i
            (self.L[i], self.L[self._right_child(i)]) = (self.L[self._right_child(i)], self.L[i])
            self.down_heapify(self._right_child(i))
            return

    def up_heapify(self,i):
        if i==0:
            return
        par = self._parent(i)
        if self.L[par] > self.L[i]:
            self.Ref[self.L[par][1]], self.Ref[self.L[i][1]] = i, par
            self.L[par], self.L[i] = self.L[i], self.L[par]
            self.up_heapify(par)
        return

    def decrease_key(self, i, newval):
        node = self.L[i]
        self.L[i][0] = newval
        self.up_heapify(i)

    def heappop(self):
        node = self.L[0]
        self.Ref.pop(self.L[0][1])
        if len(self.L)>=2:
            self.L[0] = self.L.pop()
            self.Ref[self.L[0][1]] = 0
            self.down_heapify(0)
        else:
            self.L.pop()
        return node

    def heapify(self):
        for i in range(len(self.L)-1, -1, -1):
            self.down_heapify(i)
            
            
def test():
    arr = [[2,'two'], [3, 'three'], [-11, 'minus-eleven'], [0, 'zero'], [100, 'hundred'], [30, 'thirty']]
    orig = [[2,'two'], [3, 'three'], [-11, 'minus-eleven'], [0, 'zero'], [100, 'hundred'], [30, 'thirty']]
    Ref = {}
    index = 0
    for e in arr:
        # Ref[e1] = initial pos of e1 in arr
        Ref[e[1]] = index
        index += 1
    h = Heap(arr, Ref)
    h.heapify()
    assert Ref['minus-eleven'] == 0
    h.decrease_key(Ref['thirty'], -30)
    assert Ref['thirty'] == 0
    orig[5][0] = -30
    orig.sort()
    res = []
    while arr:
        res.append(h.heappop())
    assert orig == res
    
if __name__ == '__main__':
    test()
