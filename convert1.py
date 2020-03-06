# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 15:11:15 2020

@author: 81909
"""

n = 18

# 10進数を２進数に変換
def convert(n, base):
    result = ''
    
    while n > 0:
        result = str(n % base) + result
        n //= base
        
    return result

print(convert(n, 2))
print(convert(n, 3))
print(convert(n, 8))
