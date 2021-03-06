# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 09:26:33 2020

ユークリッドの互除法
定理
2つの自然数a,bについて、aをbで割ったときの商をq,あまりをrとすると、「aとbの最大公約数」は「bとrの最大公約数」に等しい
この定理を使い、次の手順で最大公約数を求める
（１）aをbで割り、あまりr0を求める
（２）bをｒ0で割り、あまりr1を求める
（３）r0をr1で割り、あまりr2を求める
（４）あまりが０になった時点で、割る数が求める最大公約数となる

a=1274、b=975の場合
(1)1274 ÷ 975 = 1 あまり 299
(2)975 ÷ 299 = 3 あまり 78
(3)299 ÷ 78 = 3 あまり 65
(4)78 ÷ 65 = 1 あまり 13
(5)65 ÷ 13 = 5 あまり 0

最大公約数は英語で「Greatest Common Divisor」という。
@author: 81909
"""
def gcd(a, b):
# =============================================================================
#     r = a % b
#     while r != 0:
#         a, b = b, r
#         r = a % b
#     return b
# 
# =============================================================================
# 代入処理を省いて実装をシンプルにした。
    while b != 0:
        a, b = b, a % b
    return a

print(gcd(1274, 975))
