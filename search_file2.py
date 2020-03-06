# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 14:07:44 2020

ファイル検索
幅優先探索
@author: 81909
"""
import os

queue = ['d:/pg/']
file_name = 'book'

while len(queue) > 0:
    dir = queue.pop()
    for i in os.listdir(dir):
        if i == file_name:
            print(dir + i)
        if os.path.isdir(dir + i):
            if os.access(dir + i, os.R_OK):
                queue.append(dir + i + '/')
