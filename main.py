# -*- coding: utf-8 -*-
"""
Created on Sat Sep  1 21:17:25 2018

@author: ck
"""

from my_package import Foo2

if __name__ == '__main__':
    foo2 = Foo2()
    foo2.load_data(file='my_package/model/test.txt')
    print(foo2.multiply())