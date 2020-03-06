# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 15:12:26 2020
ベルマン・フォード法
辺の重みに注目して解く方法
       5
   ∞ ――――→ ∞
　4/|\ 　　 / ↑ \2 
 /1| \1 /3 |   \
0  |   ∞ 　1|　  ∞
3\ ↓       |  /4
   ∞ ――――→ ∞
       2
スタート地点は0、それ遺体の頂点は無限大に設定してから計算していく。
Pythonの場合、無限大はfloat('inf') で設定できる

頂点数をn、辺の数をmとすると、1回目の更新（内側のループ）は辺の数だけ繰り返すため、計算量は O(m)
頂点に繰り返した場合も考えると、最大でもn回繰り返して終わるので、全体の計算量は O(mn)
@author: 81909
"""
def bellman_ford(edges, num_v):
    dist = [float('inf') for i in range(num_v)]  # 初期値として無限大をセット
    dist[0] = 0# 最初の頂点のコストを0でセット
    
    changed = True  # コストが更新されている状態にセット
    while changed:
        # コストが更新されている間繰り返す
        changed = False
        for edge in edges: # 確変について繰り返し
            if dist[edge[1]] > dist[edge[0]] + edge[2]:
                # 頂点までのコストが更新できれば更新
                dist[edge[1]] = dist[edge[0]] + edge[2]
                changed = True
    return dist

# 辺のリスト（起点、終点、コストのリスト）
edges = [
    [0, 1, 4], [0, 2, 3], [1, 2, 1], [1, 3, 1],
    [1, 4, 5], [2, 5, 2], [4, 6, 2], [5, 4, 1],
    [5, 6, 4]
]
print(bellman_ford(edges, 7))

