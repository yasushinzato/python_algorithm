# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 15:25:54 2020

線形探索 O(n)
@author: 81909
"""
data = [50, 30, 90, 10, 20, 70, 60, 40, 80]
def linear_search(data, value):
    for i in range(len(data)):
        if data[i] == value:
            return i
    return -1

print(linear_search(data, 40))
    
    
