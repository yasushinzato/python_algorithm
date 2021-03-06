# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 10:57:50 2020

迷路の探索
9が壁、０が通路、１がゴール
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

# =============================================================================
# # スタート位置（x座標、y座標、移動回数をセット
# pos = [[1, 1, 0]]
# 
# while len(pos) > 0:
#     x, y, depth = pos.pop(0)  # リストから探索する位置を取得
#     
#     # ゴールに着くと終了
#     if maze[x][y] == 1:
#         print(depth)
#         break
#     
#     # 探索済みとしてセット
#     maze[x][y] = 2
#     
#     # 上下左右を探索
#     if maze[x - 1][y] < 2:
#         pos.append([x - 1, y, depth + 1]) # 移動回数を増やして左をリストに追加
#     if maze[x + 1][y] < 2:
#         pos.append([x + 1, y, depth + 1]) # 移動回数を増やして右をリストに追加
#     if maze[x][y - 1] < 2:
#         pos.append([x, y - 1, depth + 1]) # 移動回数を増やして上をリストに追加
#     if maze[x][y + 1] < 2:
#         pos.append([x, y + 1, depth + 1]) # 移動回数を増やして下をリストに追加
# =============================================================================
def search(x, y, depth):
    # ゴールにつくと終了
    if maze[x][y] == 1:
        print(depth)
        exit()
        
    # 探索済みとしてセット
    maze[x][y] = 2
    
    # 上下左右を探索
    if maze[x - 1][y] < 2:
        search(x - 1, y, depth + 1) # 移動回数を増やして左を探索
    if maze[x + 1][y] < 2:
        search(x + 1, y, depth + 1) # 移動回数を増やして右を探索
    if maze[x][y - 1] < 2:
        search(x, y - 1, depth + 1) # 移動回数を増やして上を探索
    if maze[x][y + 1] < 2:
        search(x, y + 1, depth + 1) # 移動回数を増やして下を探索
        
    # 探索前に戻す
    maze[x][y] = 0
    
# スタート位置から開始
search(1, 1, 0)
    