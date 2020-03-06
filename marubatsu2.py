# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 14:44:32 2020

3目並べ
AND演算で勝利判定。勝利判定はパターンを作成しておく。
ミニマックス法による評価値の高い最善手を探す
@author: 81909
"""

# 勝利判定パターン
goal = [
        0b111000000, 0b000111000, 0b000000111, 0b100100100,
        0b010010010, 0b001001001, 0b100010001, 0b001010100
        ]

# ３つ並んだか判定
def check(player):
    for mask in goal:
        if player & mask == mask:
            return True
    return False

# ミニマックス法
def minmax(p1, p2, turn):
    if check(p2):
        if turn:  # 自分の手番のときは勝ち
            return 1
        else:   # 相手の手番のときは負け
            return -1
        
    board = p1 | p2
    if board == 0b111111111:  # すべて埋まっていいれば引き分け
        return 0
    
    w = [i for i in range(9) if (board & (1 << i)) == 0]
    
    if turn:  # 自分の手番のときは最小値を選ぶ
        return min([minmax(p2, p1 | (1 << i), not turn) for i in w])
    else:     # 相手の手番のときは最大値を選ぶ
        return max([minmax(p2, p1 | (1 << i), not turn) for i in w])
        
# 交互に置く
def play(p1, p2, turn):
    if check(p2):   # ３つ並んでいたら出力して終了
        print([bin(p1), bin(p2)])
        return
    
    board = p1 | p2
    if board == 0b111111111:    # すべて置いたら引き分けで終了
        print([bin(p1), bin(p2)])
        return
    
    # 置ける場所を探す
    w = [i for i in range(9) if (board & (1 << i)) == 0]
    # 各場所に置いたときの評価値を調べる
    r = [minmax(p2, p1 | (1 << i), True) for i in w]
    # 評価値が一番高い場所を取得する
    j = w[r.index(max(r))]
    play(p2, p1 | (1 << j), not turn)

play(0, 0, True)

    