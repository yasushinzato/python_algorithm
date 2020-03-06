# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 12:07:42 2020
右手法による深さ探索
@author: 81909
"""
maze = [
    [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
    [9, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 9],
    [9, 0, 9, 0, 0, 0, 9, 9, 0, 9, 0, 9],
    [9, 0, 9, 9, 0, 9, 0, 0, 0, 9, 0, 9],
    [9, 0, 0, 0, 9, 0, 0, 9, 9, 0, 9, 9],
    [9, 0, 9, 0, 0, 0, 9, 9, 0, 9, 0, 9],
    [9, 9, 9, 0, 0, 9, 0, 9, 0, 0, 0, 9],
    [9, 0, 0, 0, 9, 0, 9, 0, 0, 9, 1, 9],
    [9, 0, 9, 0, 0, 0, 0, 9, 0, 0, 9, 9],
    [9, 0, 0, 9, 0, 9, 0, 0, 9, 0, 0, 9],
    [9, 0, 9, 0, 9, 0, 9, 0, 0, 9, 0, 9],
    [9, 0, 0, 0, 0, 0, 0, 9, 0, 0, 0, 9],
    [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]
]

# 右手法での移動方向'(下、右、上、左)をセット
dir = [[1, 0], [0, 1], [-1, 0], [0, -1]]

# スタート位置（x座標、ｙ座標、移動回数、方向）をセット
x, y, depth, d = 1, 1, 0, 0

while maze[x][y] != 1:
    # 探索済みとしてセット
    maze[x][y] = 2
    
    # 右手法で探索
    for i in range(len(dir)):
        # 進行方向の右側から順に探す
        j = (d + i - 1) % len(dir)   # 移動方向の個数で割って余りを求めることで、次の方向を決める
        if maze[x + dir[j][0]][y + dir[j][1]] < 2:
            # 未訪問の場合は進めて移動方向を増やす
            x += dir[j][0]
            y += dir[j][1]
            d = j
            depth += 1
            break
        elif maze[x + dir[j][0]][y + dir[j][1]] == 2:
            # 訪問済みの場合は進めて移動回数をへらす
            x += dir[j][0]
            y += dir[j][1]
            d = j
            depth -= 1
            break
        
print(depth)