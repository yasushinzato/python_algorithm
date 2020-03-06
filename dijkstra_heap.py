# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 08:40:31 2020

ダイクストラ法（ヒープによる優先度付きキューを実装）
ある頂点に接続している頂点を候補とし、その中からコストが最も小さくなる頂点を選択することを繰り返して探索する方法

ベルマン・フォード法　はすべての辺に対して処理を繰り返すが、ダイクストラ法は選択する頂点を工夫して効率よく最短経路を探す。
       5
   ∞ ――――→ ∞
　4/|\ 　　 / ↑ \2 
 /1| \1 /3 |   \
0  |   ∞ 　1|　  ∞
3\ ↓       |  /4
   ∞ ――――→ ∞
       2
       
拡張点から調べるのは1回だけ。辺の数をmとすると O(m)。
アルゴリズム全体では O(m+n^2)
@author: 81909
"""

def min_heapify(data, i):
    left = 2 * i + 1
    right = 2 * i + 2
    min = i
    if left < len(data) and data[i][0] > data[left][0]:
        min = left # 左のほうが小さい場合は、最小値の位置に左をセット
    if right < len(data) and data[min][0] > data[right][0]:
        min = right # 右のほうが小さい場合は、最小値の位置に右をセット
    if min != i:
        # 最小値が初期値から更新されたら、最小値の位置と交換して再帰処理
        data[i], data[min] = data[min], data[i]
        min_heapify(data, min)
    
def dijkstra(edges, num_v):
    dist = [float('inf')] * num_v
    dist[0] = 0
    q = [[0, 0]]
    
    while len(q) > 0:
        # キューから最小の要素を取り出し
        q[0], q[-1] = q[-1], q[0]
        _, u = q.pop()
        # キューを再構成
        min_heapify(q, 0)
        # 各辺に対してコストを調べる
        for i in edges[u]:
            if dist[i[0]] > dist[u] + i[1]:
                dist[i[0]] = dist[u] + i[1]
                q.append([dist[u] + i[1], i[0]])
                j = len(q) - 1
                while (j > 0) and (q[(j - 1) // 2] < q[j]):
                    # 親のほうが小さければ親と交換
                    q[(j - 1) // 2], q[j] = q[j], q[(j - 1) // 2]
                    j = (j - 1) // 2
    return dist

# 辺のリスト（終点とコストのリスト）
edges = [
    [[1, 4], [2, 3]],  # 頂点Aからの辺のリスト
    [[2, 1], [3, 1], [4, 5]],  # 頂点Bからの辺のリスト
    [[5, 2]],  # 頂点Cからの辺のリスト
    [[4, 3]],  # 頂点Dからの辺のリスト
    [[6, 2]],  # 頂点Eからの辺のリスト
    [[4, 1], [6, 4]],  # 頂点Fからの辺のリスト
    [] # 頂点Gからの辺のリスト
]

print(dijkstra(edges, 7))