# -*- coding: utf-8 -*-
"""
Created on Sat Sep  1 21:17:45 2018

@author: ck
"""

class Foo1:
    def __init__(self, m=None, n=None):
        self.m = m
        self.n = n
        
    def add(self):
        return self.m + self.n
    
if __name__ == '__main__':
    foo1 = Foo1(1,2)
    print(foo1.add())