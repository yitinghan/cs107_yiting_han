#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date : Thur Oct 21 2021
Coder : Yiting Han
Listener : Haoming Chen
"""
class my_node:
    
    def __init__(self, value, derivative):
        self.value = value
        self.derivative = derivative
        
    def __pow__(self, r):
        v = self.value ** r
        d = r * (self.value ** (r-1)) * self.derivative 
        return my_node(v,d)
        
if __name__ == "__main__":
    x = my_node(3,1)
    f = x ** 4
    print(f.value, f.derivative)


