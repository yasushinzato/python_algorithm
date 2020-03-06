# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 13:19:21 2020

@author: 81909
"""

for i in range(1, 51):
    # 改行せずに空白を付けて出力
    if (i % 3 == 0) and (i % 5 == 0):
        print('FizzBuzz', end=' ')
    elif i % 5 == 0:
        print('Buzz', end=' ')
    elif i % 3 == 0:
        print('Fizz', end=' ')
    else:
        print(i, end=' ') 