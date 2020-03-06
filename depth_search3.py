# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 10:38:05 2020

深さ優先探索
通りがけ順
@author: 81909
"""
tree = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14], [],[],[],[],[],[],[],[]]

def search(pos):
    if len(tree[pos]) == 2:  # 子が２つあるとき
        search(tree[pos][0])
        print(pos, end=' ')  # 左のノードと右のノードの間に出力
        search(tree[pos][1])
    elif len(tree[pos]) == 1: # 子が１つのとき
        search(tree[pos][0])
        print(pos, end=' ')  # 左のノードを調べたあとに出力
    else:  # 配下のノードがないとき
        print(pos, end=' ')
        
search(0)

