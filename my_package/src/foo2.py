# -*- coding: utf-8 -*-
"""
Created on Sat Sep  1 21:20:17 2018

@author: ck
"""

import pandas as pd
from foo1 import Foo1

class Foo2(Foo1):
    def __init__(self, m=None, n=None):
        super(Foo2, self).__init__(m, n)
    
    def load_data(self, file='../model/test.txt'):
        df = pd.read_csv(file, sep = ',', header = None)
        self.m = df[0][0]
        self.n = df[1][0]
    
    def multiply(self):
        return self.m*self.n
    
if __name__ == '__main__':
    #foo2 = Foo2(1,2)
    #print(foo2.multiply())
    
    foo2 = Foo2()
    foo2.load_data()
    print(foo2.multiply())